import json

# #格式化输出
# jsonObj = json.dumps(data, sort_keys=True, indent=4 )
# print(jsonObj)


'''
json.loads
将已编码的JSON字符串解码成Python对象
JSON     --- Python
object       dict
array        list
string       unicode
number(int)  int, long
number(real) float
true         True
false        False
null         None
'''
jsonData ='{"a":[1,2,3],"b":"bbb", "c":5, "d":4.5,"e":true,"f":false,"g":null}'
pythonData = json.loads(jsonData)
for (k,v) in pythonData.items():
    print(k, v, type(v), sep="=====")

'''
json.dumps
将Python对象编程成JSON字符串
Python            ----- JSON
dict                    object
list, tuple             array
str, unicode            string
int,loing, float        number
True                    true
False                   false
None                    null
'''
pythonDatas = [[1,2,3], (1,2), "aaaa", 4, 4.5, True, False, None]

for pythonData in pythonDatas:
    print(type(pythonData))
    jsonData = json.dumps(pythonData, indent=4)
    print(jsonData)