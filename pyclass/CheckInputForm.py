class CheckInputForm:
    __language_list = ['py', 'java']
    __check_condition_list = ['input','no-input','exact-match','ignore-space','sensitive','insensitive']
    __error_response = {}
    def __init__(self,k):
        self.__markdown = str(k.get('markdown'))
        self.__lang = str(k.get('language'))
        self.__code = str(k.get('code'))
        self.__check_condition = k.get('check_condition')
        self.__input = str(k.get('input'))
        self.__output = str(k.get('output'))
        self.__check_element = k.get('check_element')
        self.__run_option = k.get('run_option')
        
    def isInValid(self):
        b = False
    
        found = False
        try:
            for i in self.__run_option:
                if 'filename=' in i:
                    found = True
        except TypeError:
            self.__error_response['RunOption'] = 'Syntax [run-option]:# is undefind.'
            return True
                
        if not found:
            b=True
            self.__error_response['RunOption'] = 'Require filename or mainclass'
        else:
            pass

        if (self.__lang == 'None') or (self.__lang not in self.__language_list):
            b = True
            self.__error_response['Language'] = 'Part of language is not supported'

        if (self.__code.strip() == '') or (self.__code == 'None'):
            b = True
            self.__error_response['Code'] = 'Part of code is empty.'

        if (self.__check_condition == None) or(self.__check_condition == []) or (not (all(i in self.__check_condition_list for i in self.__check_condition))):
            b = True
            self.__error_response['Condition'] = 'Error in part of check-condition.'
        
        elif 'input' in self.__check_condition and (self.__input=='' or self.__input=='None'):
            b = True
            self.__error_response['Input'] = 'Part of input is empty. Require part of ::start-input:: and ::end-input::'
        if self.__output == '' or self.__output=='None':
            b = True
            self.__error_response['Output'] = 'Part of output is empty. Require part of ::start-output:: and ::end-output::'

        return b
    def getMarkdown(self):
        return self.__markdown
    def getLanguage(self):
        return self.__lang
    def getCode(self):
        return self.__code
    def getCheckCondition(self):
        return self.__check_condition
    def getInput(self):
        return self.__input
    def getOutput(self):
        return self.__output
    def getCheckElement(self):
        return self.__check_element
    def getErrorRes(self):
        return self.__error_response
    def getRunOperation(self):
        return dict(s.split('=') for s in self.__run_option)
    def getFilename(self):
        for i in self.__run_option:
            if 'filename=' in i:
                return i.replace('filename=','')+'.'+self.__lang
        return None 
    def __str__(self) -> str:
        return "\n"+ str(self.__markdown) +"\n"+ str(self.__lang) +"\n"+ str(self.__code) +"\n"+ str(self.__check_condition) +"\n"+ str(self.__input) +"\n"+ str(self.__output) +"\n"+ str(self.__check_element)