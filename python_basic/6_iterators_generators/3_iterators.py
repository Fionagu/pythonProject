class yrange:
    def __init__(self, n):
        self.a = int(input('Enter the first term\t:'))
        self.d = int(input('Enter the common difference\t:'))
        self.i = self.a
        self.n = n
    
    def _iter_(self):
        return self

    def _next_(self):
        if self.i < self.n:
            r = self.i
            self.i = self.i + self.d
            return r
        else:
            raise StopIteration

y= yrange
y.__init__(y,8)
print(y)
print(y._next_(y))
print(y._next_(y))
print(y._next_(y))
# print(y._next_(y))
# print(y._next_(y))