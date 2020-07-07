# reversed() method returns an iterator that accesses the given sequence in the reverse order.

#For string
raw_string_1 = '12345'
reversed_string_1 = reversed(raw_string_1)    #<class 'reversed'>
print(type(reversed_string_1))
print(reversed_string_1)
print(''.join(reversed_string_1))

#For tuple
raw_tuple_1=('x','y','z')
reversed_tuple_1 = reversed(raw_tuple_1)      #<class 'reversed'>
print(type(reversed_tuple_1))
print(reversed_tuple_1)
print(tuple(reversed_tuple_1))

#For string - reversed() function
raw_list_1=['a','b','c']
reversed_list_1 = reversed(raw_list_1)        #<class 'list_reverseiterator'>
print(type(reversed_list_1))
print(reversed_list_1)
print(list(reversed_list_1))

#For string - reverse() function
raw_list_2 = ['Red','Blue','Green']
raw_list_2.reverse()
print(raw_list_2)

#For string - slice
raw_list_3 = ['Windows', 'macOS', 'Linux']
reversed_list_3=raw_list_3[::-1]
print(reversed_list_3)
