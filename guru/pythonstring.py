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