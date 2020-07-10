def if_state():
    x,y=10,8
    str = 'x is < y ' if (x<y) else 'x is >= y'
    print(str)


# Python language doesn’t have a switch statement.
# Python uses dictionary mapping to implement switch statement in Python
def switch_state(argument):
    swithcer = {
        0:'this is case zero',
        1:'this is case one',
        2:'this is case three'
    }
    return swithcer.get(argument,'nothing')

if __name__=='__main__':
    if_state()
    print(switch_state(2))
