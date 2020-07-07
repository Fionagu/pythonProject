Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print((Dict['Tiffany']))

#Copying dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)

#Updating Dictionary
Dict.update({'Sarah':'9'})
print(Dict)

#Delete Keys from the dictionary
del Dict['Charlie']
print(Dict)

#Dictionary items() Method
print('Students Name: %s' %list(Dict.items()))

#Check if a given key already exists in a dictionary
print(list(Dict.items()))
print(list(Boys.items()))

for key in Dict.keys():
    if key in Boys.keys():
        print('True')
    else:
        print('False')

#Sorting the Dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
    print(":".join((S,str(Dict[S]))))

#Dictionary len() Method
print(len(Dict))

print("variable Type: %s" %type (Dict))

#Dictionary Str(dict)
print(str(Dict))
