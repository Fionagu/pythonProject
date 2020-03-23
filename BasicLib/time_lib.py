import time


# 时间获取
# print(time.time())

# print(time.ctime())

# print(time.gmtime())

#时间格式化
t = time.gmtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', t))
print(time.strftime('%Y-%B-%d %H:%M:%S', t))
print(time.strftime('%Y-%b-%d %H:%M:%S\n', t))


print(time.strftime('%Y-%b-%d %A %H:%M:%S', t))
print(time.strftime('%Y-%b-%d %a %H:%M:%S\n', t))

print(time.strftime('%Y-%m-%d %H:%M:%S', t))
print(time.strftime('%Y-%m-%d %I%p:%M:%S', t))


timeStr = '2018-01-26 12:55:20'
t = time.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
print(t)


# 程序计时
start = time.perf_counter()
end = time.perf_counter()
print(end - start)