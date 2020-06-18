# Illustration 6.14
# Given a list containing temperatures in Celsius, generate a list containing temperatures in Kelvin.

def i_6_14():
    L_Cel = [21.2,56.6,89.2,90.1,78.1]
    L_Kelvin = [x+273.16 for x in L_Cel]
    print('The output list')
    for i in L_Kelvin:
        print(i)


# Illustration 6.15
# Find the Cartesian product of two given sets.

def i_6_15():
    A = ['a','b','c']
    B = [1,2,3,4]
    AXB = [(x,y) for x in A for y in B]
    for i in AXB:
        print(i)


if __name__=='__main__':
    # i_6_14()
    i_6_15()