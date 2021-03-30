from func_decorator import *


@print_func_name
def access_dictionary():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print(thisdict['model'])

    print(thisdict.get('model'))

    print(thisdict.keys())

    print(thisdict.values())

    print(thisdict.items())

    if 'model' in thisdict:
        print('Yes, model is one of the keys in the dictionary')


@print_func_name
def change_values():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdict['year']=2018
    print(thisdict)


@print_func_name
def update_dictionary():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdict.update({'year':2018})

    thisdict.update({'color':'red','size':'big'})
    print(thisdict)


@print_func_name
def add_item():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)



@print_func_name
def remove_with_specified_key_using_pop():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)


@print_func_name
def remove_last_using_popitem():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    thisdict.popitem()
    print(thisdict)


@print_func_name
def clear_dict():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    thisdict.clear()
    print(thisdict)


@print_func_name
def loop_using_for():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    for x in thisdict:
        print(x)
        print(thisdict[x])

    for x in thisdict.keys():
        print(x)

    for x in thisdict.values():
        print(x)

    for x in thisdict.items():
        print(x)


@print_func_name
def copy_dict_using_copy():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    mydict = thisdict.copy()
    print(mydict)


@print_func_name
def copy_dict_using_dict():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    mydict= dict(thisdict)
    print(mydict)

if __name__=='__main__':
    # Access
    access_dictionary()

    # Change
    change_values()

    update_dictionary()

    # Add
    add_item()

    update_dictionary()
    
    # Remove
    remove_with_specified_key_using_pop()

    remove_last_using_popitem()

    clear_dict()

    # Loop
    loop_using_for()

    # Copy
    copy_dict_using_copy()

    copy_dict_using_dict()

    