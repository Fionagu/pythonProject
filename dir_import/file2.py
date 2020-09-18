#导入下级模块，
# 在下级目录中新建一个恐怖de __init__.py文件
from dir3 import file3

def file_2():
    print('this is file 2')


if __name__=='__main__':
    file_2()
    file3.file_3()