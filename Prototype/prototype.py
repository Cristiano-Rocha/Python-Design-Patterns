import copy

class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type
    
    def getValue(self):
        return self._value


class Type1(Prototype):
    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)

    class Type2(Prototype):
        def __init__(self, number):
            self.type = "Type2"
            self._value = number

class ObjectFactoy:
    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactoy.__type1Value1 = Type1(1)
        ObjectFactoy.__type1Value2 = Type1(2)
        ObjectFactoy.__type2Value1 = Type1(1)
        ObjectFactoy.__type2Value2 = Type1(2)

    @staticmethod
    def getType1Value1():
        return ObjectFactoy.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactoy.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactoy.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactoy.__type2Value2.clone()


def main():
    ObjectFactoy.initialize()

    instance = ObjectFactoy.getType1Value1()
    print("%s: %s" %(instance.getType(), instance.getValue()))

    instance = ObjectFactoy.getType1Value2()
    print("%s: %s" %(instance.getType(), instance.getValue()))

    instance = ObjectFactoy.getType2Value1()
    print("%s: %s" %(instance.getType(), instance.getValue()))

    instance = ObjectFactoy.getType2Value2()
    print("%s: %s" %(instance.getType(), instance.getValue()))

if __name__ == '__main__':
    main()