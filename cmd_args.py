
'''
自定义参数创建自己的Python命令行
'''
import argparse
from distutils.util import strtobool

'''
> cmd_args.py fiona qa
> cmd_args.py fiona qa --address "xxx xxx"   #address 包含多个单词，必须要双引号
> cmd_args.py fiona qa --isFullTime=False
'''
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This script is going to create an empolyeeprofile.')

    #定义位置参数
    parser.add_argument('name', help="Name of Empoyee")
    parser.add_argument('title', help='Job Title of Empoyee')

    #定义可选参数
    parser.add_argument('--address', help='Address of Empoyee')

    #定义Boolean参数
    parser.add_argument('--isFullTime', default=True, type=strtobool, help='Is this Empoyee Full Time? (default: %(default)s')

    #定义输入参数范围
    parser.add_argument('--country', choices=['Singapore','US','Malaysia'], help='Country/Region of Empoyee')

    args = parser.parse_args()
    Name = args.name
    Title = args.title
    Address = args.address
    FullTime = args.isFullTime
    Country = args.country

    print('Name is : '+ Name)
    print('Title is : '+ Title)
    print('Address is : '+ str(Address))
    if FullTime:
        print(Name+' is a full time employee')
    else:
        print(Name +' is not a full time employee')
    print('Country is : '+ str(Country))