from func_decorator import *


@print_func_name
def access_tuple():
    thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[1])

    print(thistuple[-1])

    print(thistuple[2:5])

    print(thistuple[-4:-1])

    if 'apple' in thistuple:
        print('Yes, apple is in the list')


@print_func_name
def loop_using_for():
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)


@print_func_name
def loop_using_index():
    thistuple = ("apple", "banana", "cherry")
    for i in range(len(thistuple)):
        print(thistuple[i])


@print_func_name
def loop_using_while():
    thistuple = ("apple", "banana", "cherry")
    i=0
    while i < len(thistuple):
        print(thistuple[i])
        i+=1


@print_func_name
def join_using_operator():
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1,2,3)
    
    tuple3 = tuple1+tuple2
    print(tuple3)

    tuple4 = tuple1*2
    print(tuple4)



# NewToMe: unpack a collection - tuple
def unpack_a_tuple():
    x,y,z = ('apple', 'banana','cherry')
    print(x,y,z)

    thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    x,y,*z = thistuple
    print(x,y,z)

    x,*y,z = thistuple
    print(x,y,z)


if __name__=='__main__':
    # Access
    access_tuple()

    # Loop
    loop_using_for()

    loop_using_index()

    loop_using_while()

    # Join
    join_using_operator()

    # Unpack
    unpack_a_tuple()
    