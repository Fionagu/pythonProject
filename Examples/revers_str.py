# 函数递归

# 字符串反转
def rvs(s):
    if s=='':
        return s
    else:
        return rvs(s[1:])+s[0]

