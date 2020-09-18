class myClass():
    def method1(self):
        print('Guru99')


class childClass(myClass):
    def method1(self):
        # myClass.method1(self)
        print('childClass method1')


    def method2(self):
        print('ChildClass method2')


class User:
    name = ''

    def __init__(self,name):
        self.name = name

    def sayHello(self):
        print('welcome to Guru99, '+self.name)


def main():
    c2 = childClass()
    c2.method1()
    c2.method2()

    user1 = User("Alex")
    user1.sayHello()

if __name__=='__main__':
    main()