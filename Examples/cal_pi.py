from random import random
from time import perf_counter

# V1
pi = 0
N = 100

for k in range(N):
    pi += 1/pow(16,k)*( \
        4/(8*k+1) - 2/(8*k+4) -\
            1/(8*k+5) - 1/(8*k+6))

print('Pi is {}'.format(pi))

# V2 蒙特卡罗方法
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("pi is :{}".format(pi))
print('run time is {:.5f}s'.format(perf_counter() - start))
