from func_decorator import *


@print_func_name
def access_set():
    '''Cannot access items in a set by referring to an index or a key
    
    loop through the set items using a for loop
    or ask if a specified value is present in a set

    '''
    thistset={"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","apple"}
    
    for item in thistset:
        print(item)

    if 'apple' in thistset:
        print('Yes, apple is in the set')


@print_func_name
def add_item_using_add():
    thisset = {"apple", "banana", "cherry"}

    thisset.add("orange")

    print(thisset)


@print_func_name
def add_sets_using_update():
    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}

    thisset.update(tropical)

    print(thisset)


@print_func_name
def add_any_iterable_using_update():
    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]

    thisset.update(mylist)

    print(thisset)


@print_func_name
def remove_item_using_remove():
    thisset = {"apple", "banana", "cherry"}

    thisset.remove("banana")
    print(thisset)
    try:
        thisset.remove("a")
        print(thisset)
    except Exception as e:
        print(e)


@print_func_name
def remove_item_using_discard():
    thisset = {"apple", "banana", "cherry"}

    thisset.discard("banana")
    print(thisset)

    thisset.discard("a")
    print(thisset)


@print_func_name
def remove_last_item_using_pop():
    thisset = {"apple", "banana", "cherry"}

    x = thisset.pop()
    print(x)
    print(thisset)


@print_func_name
def clear_set():
    thisset = {"apple", "banana", "cherry"}

    thisset.clear()
    print(thisset)


@print_func_name
def loop_using_for():
    thisset = {"apple", "banana", "cherry"}

    for x in thisset:
        print(x)


@print_func_name
def join_using_union():
    set1 = {'a','b','c'}
    set2 = {1,2,3}

    set3 = set1.union(set2)
    print(set3)

    c = set1 - set2
    print(c)


@print_func_name
def join_using_update():
    set1 = {'a','b','c'}
    set2 = {1,2,3}

    set1.update(set2)
    print(set1)


@print_func_name
def keep_only_duplicates_using_intersection_update():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.intersection_update(y)
    print(x)


@print_func_name
def keep_only_duplicates_using_intersection():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.intersection(y)
    print(z)
    


@print_func_name
def keep_all_but_not_the_duplicates_using_symmetric_difference_update():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}

    x.symmetric_difference_update(y)
    print(x)


@print_func_name
def keep_all_but_not_the_duplicates_using_symmetric_difference():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}

    z = x.symmetric_difference(y)
    print(z)


if __name__=='__main__':
    # Access
    access_set()

    # Change: does not allow
    # Add

    add_item_using_add()

    add_sets_using_update()

    add_any_iterable_using_update()

    # Remove
    remove_item_using_remove()

    remove_item_using_discard()

    remove_last_item_using_pop()

    clear_set()

    # Loop
    loop_using_for()

    # Join
    join_using_union()

    join_using_update()

    keep_only_duplicates_using_intersection_update()

    keep_only_duplicates_using_intersection()

    keep_all_but_not_the_duplicates_using_symmetric_difference_update()

    keep_all_but_not_the_duplicates_using_symmetric_difference()
    