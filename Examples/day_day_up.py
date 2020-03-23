# Example 1
# 一年 365 天，每天进步 1‰，累计进步多少呢
# pow(1.001, 365)
# 一年 365 天，每天退步 1 ‰，累计剩下多少呢
# pow(0.999, 365)

dayup0 = pow(1.001, 365)
daydown0 = pow(0.999, 365)

print('1‰向上：{:.2f}, 向下：{:.2f}'.format(dayup0, daydown0))

# Example 2
# 一年 365 天，每天进步 5‰ 或 1%，累计进步多少呢
# pow(1.005, 365) pow(1.01, 365)
# 一年 365 天，每天退步 5‰ 或 1%，累计剩下多少呢
# pow(0.995, 365) pow(0.99, 365)

dayfactor1 = 0.005
dayfactor2 = 0.01
dayup1 = pow(1 + dayfactor1, 365)
daydown1 = pow(1 - dayfactor1, 365)

dayup2 = pow(1 + dayfactor2, 365)
daydown2 = pow(1 - dayfactor2, 365)

print('5‰向上：{:.2f}, 5‰向下：{:.2f}'.format(dayup1, daydown1))
print('1%向上：{:.2f}, 1%向下：{:.2f}'.format(dayup2, daydown2))

#一年 365 天，一周 5 个工作日，每 天进步 1%
#一年 365 天， 一周 2 个休息日 每天退步 1%
#这种工作日的力量，如何呢？

workdayup = 1.0
workdayfactor = 0.01

for i in range(365):
    if i % 7 in [6, 0]:
        workdayup = workdayup * (1 - workdayfactor)
    else:
        workdayup = workdayup * (1 + workdayfactor)
print('工作日的力量：{:.2f}'.format(workdayup))

#Example 4
#工作日模式要努力到什么水平，才能与每天努力 1% 一样？
#A 君 : 一 年 365 天，每天进步 1%1%，不停歇
#B 君 : 一 年 365 天 ，每周工作 5 天休息 2 天，休息日下降 1%1%，要 多 努力呢？


def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print('工作日的努力参数是：{:.3f}'.format(dayfactor))