import os


class Isolate:
    __init_isolate = 'isolate --cg --init'
    __run_isolate = 'isolate -p --cg --run'
    __clean_isolate = 'isolate --cg --cleanup'
    __env_py = '--env=HOME=/home/pong'
    __meta = '--meta=meta.txt'
    __location_py = '/usr/bin/python3'
    __location_javac = '/usr/lib/jvm/java-11-openjdk-amd64/bin/javac'
    __location_java = '/usr/lib/jvm/java-11-openjdk-amd64/bin/java'
    __stdin = '--stdin='
    __stdout = '--stdout=out.txt'
    __stderr = '--stderr=err.txt'
    __std = __stdin+' '+__stdout+' '+__stderr
    __isolatepath = '/var/local/lib/isolate/'

    def __init__(self, id) -> None:
        self.__id = str(id)
        self.__isolatepath = self.__isolatepath+str(id)+'/box/'
        self.__std = self.__std+' '+'--meta='+self.__isolatepath+'meta.txt'
        self.__meta = '--meta='+self.__isolatepath+'meta.txt'

    def init(self):
        bid = '--box-id='+self.__id
        sl = self.__init_isolate + ' ' + bid
        os.system(sl)

    def clean(self):
        bid = '--box-id='+self.__id
        sl = self.__clean_isolate + ' ' + bid
        os.system(sl)

    def getBid(self) -> str:
        return '--box-id='+self.__id

    def getId(self) -> str:
        return self.__id

    def getRun(self) -> str:
        return self.__run_isolate

    def getStd(self) -> str:
        return self.__std

    def getEnvPy(self) -> str:
        return self.__env_py

    def getMeta(self) -> str:
        return self.__meta

    def getLocationJava(self) -> str:
        return self.__location_java

    def getLocationJavac(self) -> str:
        return self.__location_javac

    def getLocationPy(self) -> str:
        return self.__location_py

    def getIsoPath(self) -> str:
        return self.__isolatepath

    def getMeta(self) -> str:
        return self.__meta

    def getStdin(self) -> str:
        return self.__stdin

    def getStdout(self) -> str:
        return self.__stdout

    def getStderr(self) -> str:
        return self.__stderr
