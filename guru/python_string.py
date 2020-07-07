x="Guru"
print (x[2])
print(x[1:3])
print('u' in x)
print('1' not in x)

#Raw string suppresses actual meaning of escape characters.
x=R"prints R'\n' prints \n"
print(x)

#% - Used for string format
name = 'guru'
number = 99
print('%s %d' %(name, number))

x='guru'
y='99'
print(x+y)
print(x*2)

#replace()
oldstring = 'I like Guru99'
newstring = oldstring.replace('like','love')
print(oldstring)
print(newstring)

#Changing upper and lower case strings
string='python at guru99'
print(string.upper())
print(string.capitalize())

string='PYTHON AT GUGU99'
print(string.lower())

#Using "join" function for the string
print(":".join("Python"))

#Reversing String
raw_string='12345'
reversed_string=reversed(raw_string)
print(type(reversed_string))
print(reversed_string)
# for i in reversed_string:
#     print(i,end=' ')
print(''.join(reversed_string))
print('\n')

raw_list=['a','b','c']
print(raw_list)
raw_list.reverse()
print(raw_list)
reversed_list=reversed(raw_list)
print(type(reversed_list))
print(reversed_list)
# for i in reversed_list:
#     print(i,end=' ')
print(''.join(reversed_list))
print('\n')

raw_tuple=('x','y','z')
reversed_tuple=reversed(raw_tuple)
print(type(reversed_tuple))
print(reversed_tuple)
# for i in reversed_tuple:
#     print(i,end=' ')
print(''.join(reversed_tuple))
