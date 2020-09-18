#导入上级模块
#需要当前执行目录为dir4
import sys
sys.path.append('..')
import file1
from dir3 import file3

def file_4():
    print('this is file 4')

if __name__=='__main__':
    file_4()
    file1.file_1()
    file3.file_3()