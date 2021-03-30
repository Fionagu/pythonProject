from func_decorator import *


@print_func_name
def access_list():
    # print('------access_list------')
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

    print(thislist[1])
    print(thislist[-1])
    print(thislist[2:5])
    print(thislist[-4:-1])

    if 'apple' in thislist:
        print('Yes, apple is in the list')


@print_func_name
def change_item_values():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

    thislist[0] = 'blackcurrant'
    print(thislist)

    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)

    thislist[1:3] = ["mango"]
    print(thislist)

    thislist[1:3] = "mango"
    print(thislist)


@print_func_name
def insert_items():
    thislist = ["apple", "banana", "cherry"]

    thislist.insert(2, "watermelon")
    print(thislist)


@print_func_name
def add_using_append():
    thislist = ["apple", "banana", "cherry"]
    
    thislist.append("orange")
    print(thislist)

    thislist.append("orange")
    print(thislist)


@print_func_name
def add_using_extend():
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]

    thislist.extend(tropical)
    print(thislist)


@print_func_name
def add_any_iterable():
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")

    thislist.extend(thistuple)
    print(thislist)

@print_func_name
def remove_specified_item_using_remove():
    thislist = ["apple", "banana", "cherry"]

    thislist.remove("banana")
    print(thislist)


@print_func_name
def remove_specified_index_using_pop():
    thislist = ["apple", "banana", "cherry","orange"]
    print(thislist)

    poped = thislist.pop()
    print('poped item is', poped)
    print(thislist)

    poped = thislist.pop(1)
    print('poped item is', poped)
    print(thislist)


@print_func_name
def clear_list():
    thislist = ["apple", "banana", "cherry"]

    thislist.clear()
    print(thislist)


@print_func_name
def loop_using_for():
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)


@print_func_name
def loop_using_index():
    thislist = ["apple", "banana", "cherry"]
    for i in range(len(thislist)):
        print(thislist[i])


@print_func_name
def loop_using_while():
    thislist = ["apple", "banana", "cherry"]
    i=0
    while i < len(thislist):
        print(thislist[i])
        i+=1


@print_func_name
def loop_using_list_comprehension():
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]



@print_func_name
def list_comprehension():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if 'a' in x]
    print(newlist)
    

@print_func_name
def sort_default_alphanumbrically_acscending():
    fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
    fruits.sort()
    print(fruits)   

    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist)


@print_func_name
def sort_descending():
    fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
    fruits.sort(reverse = True)
    print(fruits)


def my_sort_func(n):
    return abs(n-50)

@print_func_name
def customize_sort_using_key():
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=my_sort_func)
    print(thislist)


@print_func_name
def sort_case_insensitive():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key = str.lower)
    print(thislist)


@print_func_name
def reverse_order():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    print(thislist)



@print_func_name
def copy_list_using_copy():
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)


@print_func_name
def copy_list_using_list():
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)



@print_func_name
def join_using_operator():
    list1 = ["apple", "banana", "cherry"]
    list2 = [1,2,3]
    
    list3 = list1+list2
    print(list3)

    list4 = list1*2
    print(list4)


@print_func_name
def join_using_extend():
    list1 = ["apple", "banana", "cherry"]
    list2 = [1,2,3]
    list1.extend(list2)

    print(list1)


# NewToMe: unpack a collection - list
def unpack_a_list():
    x,y,z = ['apple', 'banana','cherry']
    print(x,y,z)

    thistuple=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    x,y,*z = thistuple
    print(x,y,z)

    x,*y,z = thistuple
    print(x,y,z)


if __name__=='__main__':
    # Access
    access_list()

    # Change
    change_item_values()

    insert_items()

    # Add
    add_using_append()

    insert_items()

    add_using_extend()

    add_any_iterable()

    # Remove
    remove_specified_item_using_remove()

    remove_specified_index_using_pop()

    clear_list()

    # Loop

    loop_using_for()

    loop_using_index()

    loop_using_while()

    loop_using_list_comprehension()

    # List Comprehension
    list_comprehension()

    # Sort
    sort_default_alphanumbrically_acscending()

    sort_descending()

    customize_sort_using_key()

    sort_case_insensitive()

    reverse_order()

    # Copy
    copy_list_using_copy()

    copy_list_using_list()

    # Join

    join_using_operator()

    join_using_extend()

    unpack_a_list()


