class A:
    def method(self):
        print('A method')


class B(A):
    pass


class C(A):
    def method(self):
        print('C method')


class D(B, C):
    pass

for cls in [A,B,C,D]:
    print(cls.__name__ , ':', cls.__mro__)

obj = D()
obj.method()
print(D.__mro__)

print(isinstance(obj, A))
print(issubclass(D, A))