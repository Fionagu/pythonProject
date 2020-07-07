# Packing and unpacking

#In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

x = ('Guru99',20,'Education')
(company, emp, profile)=x
print(company)
print(emp)
print(profile)

# Comparing tuples
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

#error usage:TypeError: '>' not supported between instances of 'int' and 'str'
a=(5,6)
b=('a','b')
if (a>b):print("a is bigger")
else: print ("b is bigger")

#Tuples and dictionary
#-----Dictionary can return the list of tuples by calling items, where each tuple is a key value pair.
a={'x':100,'y':200}
b = list(a.items())
print(b)

#error usage: AttributeError: 'tuple' object has no attribute 'key'
for item in a.items():
    print(item.key +'\t'+item.value)

#Using tuples as keys in dictionaries
#directory[last,first] = number


# Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])

#delete a tuple
# del

# Built-in functions with Tuple
# To perform different task, tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.