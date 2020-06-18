# Illustration 6.5
# Using iterators the program puts the positive and negative numbers of a list into two separate lists and raises an error at the end of the program.


def i_6_5():
    L = [1, 2, 3, -4, -5, -6]
    P, N = [], []
    t = iter(L)
    try:
        while True:
            x = t.__next__()
            if x >= 0:
                P.append(x)
            else:
                N.append(x)
    except StopIteration as e:
        print('origin List-',L,'\nList containing the positive number- ',P,'\nList containing the negative numbers-',N)
    raise StopIteration


# Illustration 6.6
# Write a program that uses iterators to separate the vowels and consonants of a given string and raises an error at the end of the program.

def i_6_6():
    s='color'
    vow, cons = '',''
    t = iter(s)
    try:
        while True:
            x=t.__next__()
            if x in ['a','e','o','u','i']:
                vow+=x
            else:
                cons+=x
    except StopIteration:
        print('String - '+s+'\nVowels - '+vow+'\nConsonents - '+ cons)
    raise StopIteration


# Illustration 6.7
# Write a program to add the corresponding elements of two given lists and sort the final list.

def i_6_7():
    l1 = [3,6,1,8,5]
    l2 = [7,4,6,2,9]
    i1 = iter(l1)
    i2 = iter(l2)
    l3 = sorted(list(i1)+list(i2))
    print('List1 - ',l1,'\nList2 - ',l2,'\nSortedCombn - ', l3)


if __name__=='__main__':
    # i_6_5()
    # i_6_6()
    i_6_7()