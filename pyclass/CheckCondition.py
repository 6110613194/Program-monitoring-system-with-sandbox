from difflib import SequenceMatcher
import json
class CheckCondition:
    def __init__(self,rsc,dict_k) -> None:
        self.__rsc = rsc
        self.__lc = dict_k.get('check_condition')
        self.__dict_k = dict_k
        self.__dict_answer = {}
        self.count = 0
    def check(self):
        if 'exact-match' in self.__lc:
            case = 'exact-match'
            output_from_dict = self.__dict_k.get('output')
            output_cp = self.__rsc
            percent = round(SequenceMatcher(None, output_from_dict, output_cp).ratio()*100, 2)
            
            self.__dict_answer[self.countCon()] = buildJSON(case,(output_from_dict == output_cp),percent,output_from_dict,output_cp)
            
        
        if 'ignore-space' in self.__lc:
            case = 'ignore-space'
            char_to_replace = {' ':'','\n':'','\t':''}
            output_from_dict = self.__dict_k.get('output').rstrip().translate(str.maketrans(char_to_replace))
            output_cp = self.__rsc.rstrip().translate(str.maketrans(char_to_replace))
            percent = round(SequenceMatcher(None, output_from_dict, output_cp).ratio()*100, 2)
            
            self.__dict_answer[self.countCon()] = buildJSON(case,(output_from_dict == output_cp),percent,output_from_dict,output_cp)
           
        if ('insensitive' in self.__lc):
            case = 'insensitive-case'
            output_from_dict = self.__dict_k.get('output').lower()
            output_cp = self.__rsc.lower()
            percent = round(SequenceMatcher(None, output_from_dict, output_cp).ratio()*100, 2)
            self.__dict_answer[self.countCon()] = buildJSON(case,(output_from_dict == output_cp),percent,output_from_dict,output_cp)
            
        if ('sensitive' in self.__lc):
            case = 'sensitive-case'
            output_from_dict = self.__dict_k.get('output')
            output_cp = self.__rsc
            percent = round(SequenceMatcher(None, output_from_dict, output_cp).ratio()*100, 2)  
            self.__dict_answer[self.countCon()] = buildJSON(case,(output_from_dict == output_cp),percent,output_from_dict,output_cp)
        
        if self.__dict_k.get('check_element') != []:
            case = 'check_element'
            element = self.__dict_k.get('check_element')
            try:
                num_element = len(element)
            except TypeError:
                pass
            else:
                ans_true = 0
                code = self.__dict_k.get('code')
                ans = []
                for e in element:
                    if e in code:
                        ans_true=ans_true+1
                        ans.append((e,True))
                    else:
                        ans.append((e,False))
                percent = round((ans_true/num_element)*100,2)
                
                self.__dict_answer[self.countCon()] = buildJSONElement(case,percent,ans)
            
    def getDictAnswer(self):
        return json.dumps(self.__dict_answer)

    def countCon(self):
        self.count = self.count +1
        return self.count
    
def buildJSON(con,result,pscorrect,eout,yout):
    return {'Condition':con,'Result':result,'Percent-Correct':pscorrect,'Expect output':eout,'Your output':yout}

def buildJSONElement(con,pscorrect,list):
    a={}
    for kw,s in list: 
        a[kw]=s
    d = {
        'Condition':con,
        'Percent-Correct':pscorrect,
        'ElementIsFound':a
    }
    
    return d