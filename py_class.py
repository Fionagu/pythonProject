class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2009
    
    def welcome(self):
        print('Welcome {} {} to the class of {}'.format(self.fname, self.lname, self.graduationyear))


if __name__=='__main__':
    person = Person('fiona','gu')
    person.printname()

    student = Student('fiona','gu')
    student.printname()
    student.welcome()