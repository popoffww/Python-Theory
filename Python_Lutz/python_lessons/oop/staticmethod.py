class SomeObject:
    class_attr = 11

    def __init__(self):
        self.data_attr = 21

    def data_method(self):
        print(self.data_attr)

    @staticmethod
    def static_method():
        print(SomeObject.class_attr)

if __name__ == '__main__':
    SomeObject.static_method()
    obj = SomeObject()
    obj.data_method()
    obj.static_method()