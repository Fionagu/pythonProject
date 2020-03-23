# 
tempStr =input('请输入带有符号的温度值:')
if tempStr[-1] in ['F', 'f']:
    c = (eval(tempStr[0:-1]) -32)/1.8
    print('装换后的温度是{:.2f}C'.format(c))
elif tempStr[-1] in ['C', 'c']:
    f = 1.8 * eval(tempStr[0:-1])
    print('转换后的温度是{:.2f}F'.format(f))
else:
    print('输入格式错误')