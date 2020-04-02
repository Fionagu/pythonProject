# 局部变量为组合数据类型且未创建，等同于全局变量

# Exmaple 1:
ls = ['F','f'] #通过使用真实创建了一个全局变量列表 ls
def func(a):
    ls.append(a)   #此处ls 是列表类型，未真实创建则等同于全局变量
    return

func('C')
print(ls)

# Example 2:
ls2 = ['F','f']
def func_2(a):
    ls2 = []       #此处 ls2 是列表类型，真实创建,ls2 是局部 变量
    ls2.append(a)
    return

func_2('C')
print(ls2)


#lambda 函数
f= lambda x,y: x+y
print(f(5,10))