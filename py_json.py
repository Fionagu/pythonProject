import json
from func_decorator import *

# 处理字符串
# json.loads(): 解码  --- JSON 对象   ---> Python 类型
# json.dumps() : 编码 --- Python 类型 ---> JSON 对象

# 处理文件
# json.load(): 解码  --- 文件   ---> Python 类型
# json.dump() : 编码 --- Python 类型 ---> 文件


@print_func_name
def convert_from_json_to_python():
    # some JSON:
    x = '{"name":"John","age":30,"city":"New York"}'
    y = json.loads(x)
    print(x)
    print(type(y))


@print_func_name
def convert_from_python_to_json():
    # a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    y = json.dumps(x)
    print(y)


@print_func_name
def format_result_using_dumps():
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    y = json.dumps(x, indent = 4)
    print(y)

    y = json.dumps(x, indent = 4, sort_keys=True)
    print(y)

    # NewToMe: json dumps separator parameters
    # You can also define the separators, default value is (", ", ": "), 
    # which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
    y = json.dumps(x, indent = 4, sort_keys=True, separators=(". "," = "))
    print(y)


def write_json_file():
    filepath =os.path.join(os.path.split(os.path.abspath(__file__))[0],'json_write.json')

    data = {'no':1,'name':'Runoob','url':'test.com'}
    with open(filepath,'w') as f:
        json.dump(data, f)


def read_json_file():
    filepath = os.path.join(os.path.split(os.path.abspath(__file__))[0],'json_read.json')
    with open (filepath,'r') as f:
        data = json.load(f)

    print(data)


if __name__== '__main__':
    convert_from_json_to_python()

    convert_from_python_to_json()

    format_result_using_dumps()