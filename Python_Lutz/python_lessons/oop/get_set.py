class A:
    __str1 = 'Private string A'
    _str2 = 'Inner string A'
    str3 = 'Common string A'

    def __init__(self,__str1='',_str2='',str3=''):
        self.__str1 = __str1
        self._str2 = _str2
        self.str3 = str3

    def get_str(self):
        return self.__str1

    @staticmethod
    def stat_method():
        print(A.__str1)
        print(A._str2)

    def method(self):
        print(self.str3)


objA = A()
A.stat_method()
objA.stat_method()


class B(A):
    pass


objB = B()
objB.str3 = 'Common string B on objB'
objB.method()
objB.stat_method()
objB.get_str()




