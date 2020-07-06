f = 101 
print(f)

def someFunc():
    # global f
    f = 'I am learning Python'
    print(f)

someFunc()
print(f)


#use del to remove varibles
del f
print(f)