def print_func_name(func):
    def wrapper():
        print('\n------{}------'.format(func.__name__))
        func()
    return wrapper