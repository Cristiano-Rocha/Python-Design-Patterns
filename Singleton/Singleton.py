class Singleton:
    
    __instance = None
    
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This is a Singleton class")
        else:
            Singleton.__instance = self

a = Singleton()
print(a)
a = Singleton.getInstance()
print(a)
a = Singleton.getInstance()
print(a)
a = Singleton.getInstance()
print(a)