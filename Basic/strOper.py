# 字符串处理函数

print(chr(10004))

for i in range(12):
    print(chr(9800+i), end="")


# 字符串处理方法

str = 'AbCdEfGh'
print(str.lower())
print(str.upper())

str = 'A,B,C'
print(str.split(','))

str = 'a apple a day'
print(str.count('a'))

str = 'python'
print(str.replace('n','n123.io'))

print(str.center(20,'='))

str='= python='
print(str.strip(' =np'))

print(','.join('12345'))

# 字符串类型的格式化

print('{}:计算机{}的CPU占用率为{}%'.format('2018-10-10','C', 10))
print('{1}:计算机{0}的CPU占用率为{2}%'.format('2018-10-10','C', 10))

# {:<填充> <对齐> <宽度> <数字千位分隔符> <.精度> <类型>}
# < 左对齐 
# > 右对齐
# = 居中对齐
# 整数类型 b, c, d, o, x, x
# 浮点数类型 e, E, f, %
print('{0:=^20}'.format('PYTHON'))
print('{0:=<20}'.format('PYTHON'))
print('{0:=>20}'.format('PYTHON'))

print('{0:,.2f}'.format(12345.6789))
# print('{0:,.2d}'.format(12345.6789)) --- Error 

print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425))

print('{0:e},{0:E},{0:f},{0:%}'.format(3.14))