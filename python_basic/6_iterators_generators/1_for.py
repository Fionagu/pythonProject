# Illustration 6.1
# From a given list, put all the positive numbers in one list and negative numbers in the other list.

def i_6_1():
    L= [1,2,5,7,-1,3,-6,7]
    P = []
    N = []
    for num in L:
        if(num>0):
            P.append(num)
        elif(num<0):
            N.append(num)

    print('The list of positive numebers \t:',P)
    print('The list of negative numebers \t:',N)


# Illustration 6.2
# Ask the user to enter a string and put all the vowels of the string in one string and the consonants in the other string.

def i_6_2():
    string = input('Enter a string\t:')
    str1, str2= '',''
    for s in string:
        if s in ['a','e','o','i','u']:
            str1=str1+str(s)
        else:
            str2=str2+str(s)
    print('The string contains the vowels is '+str1)
    print('The string contains consonants '+str2)


# Illustration 6.3
# This illustration demonstrates the use of for for iterating through a tuple.

def i_6_3():
    T= (1,2,3)
    for i in T:
        print(i)
    print(T)



# Illustration 6.4
# This illustration demonstrates the use of for for iterating through a dictionary.

def i_6_4():
    Dictionary = {'Programming in C#':499, 'Algotithms Analysiis and Design':599}
    print(Dictionary)
    for i in Dictionary:
        print(i)


if __name__=='__main__':
    # i_6_1()
    # i_6_2()
    # i_6_3()
    i_6_4()

