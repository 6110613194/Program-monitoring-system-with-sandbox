import os

class FileOperation:
    __path = '/var/local/lib/isolate/'
    def __init__(self,id, filename):
        self.__id = id
        self.__filename = str(filename)
        self.__isolatepath = self.__path+str(id)+'/box/'

    def readFile(self):
        f = open(os.path.join(self.__isolatepath, self.__filename), "r")
        file_read = f.read()
        f.close()
        return file_read

    def readLineFile(self):
        f = open(os.path.join(self.__isolatepath, self.__filename), "r")
        file_readline = f.readlines()
        f.close()
        return file_readline

    def writeFile(self,textmd):
        f = open(os.path.join(self.__isolatepath, self.__filename), "w+")
        f.write(textmd)
        f.close()
    
    def getFilename(self)->str:
        return self.__filename
    
    def getIsopath(self)->str:
        return self.__isolatepath
        
