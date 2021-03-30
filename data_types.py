def get_data_types():
    """ build in types

    Text Type: str
    Numberic Types: int, float, complex
    Sequence Types: list, tuple, range
    Mapping Type: dict
    Set Types: set, frozenset
    Boolean Type: bool
    Binary Types: bytes, bytearray, memoryview
    """

    x = range(5)
    print('type of ', x, ' is ', type(x))

    x = frozenset({'apple','cherry'})
    print('type of ', x, ' is ', type(x))

    x= b'hello'
    print('type of ', x, ' is ', type(x))
    x=bytes(5)
    print('type of ', x, ' is ', type(x))

    x=bytearray(5)
    print('type of ', x, ' is ', type(x))

    x=memoryview(bytes(5))
    print('type of ', x, ' is ', type(x))

    x = bool(5)
    print('type of ', x, ' is ', type(x))


# NewToMe: frozen set 
def set_vs_frozenset():
    """Set VS. Frozenset

    set: 可变集合，无序排序且不重复，可变，有add(), remove()等方法，不存在哈希值，
         基本功能包含关系测试和消除重复元素，还支持unon, intersection, difference, sysmmetric difference等数学运算

    frozenset: 不可变集合,存在哈希值，好处是可以作为字典的key，缺点是一旦创建就不能更改
    
    """


if __name__=='__main__':
    get_data_types()