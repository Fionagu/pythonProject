import random

# 基本随机数函数

random.seed(10)
print(random.random())

print(random.random())


# 扩展随机数函数

print(random.randint(1,10))   # [1,10] 整数

print(random.uniform(1,10))   # [1,10] 小数

print(random.randrange(10,100,10))   #[10,100) 之间以K为步长的整数

print(random.getrandbits(16))  # 16 比特长的随机整数

print(random.choice([1,2,3,4,5,6,7])) # 随机选择一个元素

s= [1,2,3,4,5,6]
random.shuffle(s)   # 将 s 元素随机排序，返回打乱后的序列
print(s)