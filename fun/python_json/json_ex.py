import json
import os

# 处理字符串
# json.dumps() : 编码 --- Python 类型 ---> JSON 对象
# json.loads(): 解码  --- JSON 对象   ---> Python 类型

# 处理文件
# json.dump() : 编码 --- Python 类型 ---> 文件
# json.load(): 解码  --- 文件   ---> Python 类型


def python_to_json():
    data = {'no':1,'name':'Runoob','url':'test.com'}
    json_str = json.dumps(data)
    print(type(data))
    print(type(json_str))
    print('Python类型:',repr(data))
    print('JSON 对象：', json_str)

    json_str_2 = json.dumps(data, indent=4, sort_keys=True)
    print('JSON 对象：', json_str_2)


def json_to_python():
    data1 = {'no':1,'name':'Runoob','url':'test.com'}
    json_str = json.dumps(data1)

    data2 = json.loads(json_str)
    print(data2['name'])


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
    python_to_json()
    # json_to_python()
    # write_json_file()
    # read_json_file()