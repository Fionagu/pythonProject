def arithmetic_progression(a,d,n):
    i = 1
    while i<=n:
        yield (a+(i-1)*d)
        i+=1


class arithmetic_progression_class():
    def __init__(self, a,d, n):
        self.a = a
        self.d = d
        self.n = n #maximun
        self.i = self.a

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i = self.i+self.d
            return i
        else:
            raise StopIteration()



if __name__=='__main__':
    # progression=arithmetic_progression(5,3,8)
    # for i in progression:
    #     print(i)

    progression = arithmetic_progression_class(5,3,16)
    t = progression.__iter__()
    while True:
        print(t.__next__())