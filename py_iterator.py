'''
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
'''

# NewToMe: Iterator example
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    # could continue forever if you had enough next() or if it was used in a for loop
    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    # NewToMe: StopIteration statement
    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration



if __name__=='__main__':
    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))

    print('for')
    for x in myiter:
        print(x)