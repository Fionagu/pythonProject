import requests

'''
r = requests.get(url='http://www.itwhy.org') # 最基本的GET请求
print(r.status_code)

r = requests.get('http://httpbin.org/get') #GET请求
print(r.status_code)

r = requests.post('http://httpbin.org/post') #POST请求
print(r.status_code)

r = requests.put('http://httpbin.org/put') #PUT请求
print(r.status_code)

r = requests.delete('http://httpbin.org/delete') #DELETE请求
print(r.status_code)

r = requests.head('http://httpbin.org/get') #HEAD请求
print(r.status_code)

r = requests.options('http://httpbin.org/get') #OPTIONS请求
print(r.status_code)
'''

#==========带参数的请求实例
# r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  #带参数的GET请求
# print(r.url)
# print(r.request.url)

r = requests.post('http://www.itwhy.org/wp-comments-post.php', data = {'comment':'testing'})
print(r.status_code)