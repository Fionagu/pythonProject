# Illustration 6.9
# Write a generator to produce arithmetic progression where in the first term, the common difference and the number of terms is entered by the user.


def arithmetic_progression(a, d, n):
    i = 1
    while (i <= n):
        yield (a + (i - 1) * d)
        i += 1


def i_6_9():
    a = int(input('Enter the first term of the arithmetic progression\t:'))
    d = int(input('Enter the common difference of the arithmetic progression\t:'))
    n = int(input('Enter the number of terms of the arithmetic progression\t:'))

    ap = arithmetic_progression(a, d, n)
    print(ap)
    for i in ap:
        print(i)


# Illustration 6.10
# Write a generator to produce geometric progression, where in the first term the common ratio and the number of terms is entered by the user.


def geometric_progression(a, r, n):
    i = 1
    while i <= n:
        yield (a * pow(r, i - 1))
        i += 1


def i_6_10():
    a = int(input('Enter the first term of the geometric progression\t:'))
    r = int(input('Enter the common ratio of the geometric progression\t:'))
    n = int(input('Enter the number of terms of the geometric progression\t:'))

    gp = geometric_progression(a,r,n)
    for i in gp:
        print(i)


# Illustration 6.11
# Write a generator to produce a Fibonacci series.

def fib(n):
    a = [0 for i in range(0,n)]
    if n==1:
        a[0]=1
        yield 1
    elif n ==2:
        a[1]=1
        yield 1
    else:
        a[0]=1
        yield a[0]
        a[1]=1
        yield a[1]
        i = 2
        while(i<=n-1):
            a[i]=a[i-1]+a[i-2]
            yield (a[i])
            i+=1


def i_6_11():
    n = int(input('Enter the number of terms\t:'))
    fabList = fib(n)
    for i in fabList:
        print(i)
    # print(next(fabList))

# Illustration 6.12
# This illustration demonstrates the effect of yield on the value of the counter.

def demo():
    print('Start')
    for i in range(20):
        print('value of i before yield\t:', i)
        yield i
        print('value of i after yield\t:', i)
    print('End')


def i_6_12():
    a = demo()
    for i in a:
        print(i)


if __name__ == '__main__':
    # i_6_9()
    # i_6_10()
    i_6_11()
    # i_6_12()