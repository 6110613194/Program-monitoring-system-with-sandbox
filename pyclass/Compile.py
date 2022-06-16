from .CpLang import *
from pyclass.Isolate import Isolate



class Compile(Isolate):
    def __init__(self, id, filename,inputfilename, language, mem='1024', time='1') -> None:
        super().__init__(id)
        self.__filename = str(filename)
        self.__inputfilename = str(inputfilename)
        self.__language = str(language)
        self.__mem = '--cg-mem='+str(mem)
        self.__time = '--time='+str(time)

    def run(self):
        if self.__language == 'py':
            cp_run_command = self.getRun()+' '+self.getBid()+' '+self.__time+' '+self.__mem+' '+ \
                self.getStdin()+self.__inputfilename+' '+self.getStdout()+' '+self.getStderr()+ \
                ' '+self.getMeta()+ \
                ' '+self.getEnvPy()+' '+self.getLocationPy()+' '+self.__filename
            return python(self.getId(),cp_run_command)

        elif self.__language == 'java':
            cp_command = self.getRun()+' '+self.getBid()+' '+'--stderr=err.txt' + ' ' + self.getMeta() + \
                ' '+self.getLocationJavac()+' '+self.__filename
            run_command = self.getRun()+' '+self.getBid()+' '+self.__time+' '+self.__mem+' '+ \
                self.getStdin()+self.__inputfilename+' '+self.getStdout()+' '+self.getStderr()+ \
                ' '+self.getMeta()+ \
                ' '+self.getLocationJava()+' '+self.__filename.replace('.java','')
            return java(self.getId(),cp_command,run_command)



