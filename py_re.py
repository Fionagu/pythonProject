''' # NewToMe: re
.* 表示任意匹配除换行符(\n, \r)之外的任何单个或多个字符
(.*?) 表示非贪婪模式，只保存第一个匹配到的子串

match()  ---> 只匹配字符串的开始，返回匹配对象re.Match
search() ---> 匹配整个字符串，返回匹配对象re.Match
findall() ---> 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表

sub()   ---> sub中repl可以是一个函数，具体用法见 re_sub()
compile()

re.I 忽略大小写
compile之后的match方法和 re.match 不一样

'''
import re


def re_match():
    ''' match 起始位置，一个match对象

    re.match(pattern, string, flags=0): 尝试从字符串的起始位置匹配一个模式，如果不是起始位置成功匹配的话，返回none

    group(), group(0) 匹配的整个表达式的字符串

    如果pattern里group，则匹配才有group
    groups(), 包含所有小组字符串的元组
    group(1,2) 包含特定小组号的字符串
    '''

    # 没有小组
    raw = 'www.ruboo.com'
    x = re.match(r'www',raw)
    print(x)   #<re.Match object; span=(0, 3), match='www'>
    print(type(x))  #<class 're.Match'>
    print(dir(x))

    print(x.group(), x.group(0), sep='\t') #匹配的整个表达式的字符串
    print(x.groups(),x.groups(0),sep='\t')   #没有小组，所以是空的tuple

    print(x.span(),x.span(0),sep='\t')
    print(x.start(),x.start(0),sep='\t')
    print(x.end(),x.end(0),sep='\t')

    # 一下代码会出错，因为没有小组
    try:
        print(x.groups(1))
        print(x.group(1))
        print(x.span(1))
        print(x.start(1))
        print(x.end(1))
    except IndexError as e:
        print(e)

    # 有小组
    raw = 'Cats are smarter than dogs'
    matchObj = re.match(r'(.*) are (.*?) .*', raw, re.M|re.I)
    if matchObj:
        print(matchObj.groups())
        print(matchObj.group())
        print(matchObj.group(0,1,2))
        print(matchObj.group(1), matchObj.start(1), matchObj.end(1), matchObj.span(1))
        print(matchObj.group(2), matchObj.start(2), matchObj.end(2), matchObj.span(2))

        # print(matchObj.group(3)) //只有2个group


def re_search():
    raw = "Cats are smarter than dogs"

    # 没有小组
    matchObj = re.match(r'dogs', raw, re.M|re.I)
    if matchObj:
        print('match() ---> mathchObj.group(): ', matchObj.group())
    else:
        print('match() ---> no match')

    matchObj = re.search(r'dogs', raw, re.M|re.I)
    if matchObj:
        print('search() ---> mathchObj.group(): ', matchObj.group())
    else:
        print('search() ---> no match')

    # 有小组
    matchObj = re.match(r'are (.*?) .*', raw, re.M|re.I)
    if matchObj:
        print('match() ---> mathchObj.group(): ', matchObj.group())
    else:
        print('match() ---> no match')

    matchObj = re.search(r'are (.*?) .*', raw, re.M|re.I)
    if matchObj:
        print('search() ---> mathchObj.group(): ', matchObj.groups())
    else:
        print('search() ---> no match')


def re_sub():
    raw = "2004-959-559 # 这是一个电话号码"

    # delete comments
    num = re.sub(r'#.*', '',raw, re.M|re.I)
    print(num,len(num))

    matchObj = re.search(r'#.*', raw)
    if matchObj:
        print(matchObj.group())

    # 移出非数字内容
    num = re.sub(r'\D','',raw)
    print(num)

    matchObj = re.search(r'\D',raw)
    if matchObj:
        print(matchObj.group())
        print(matchObj.groups())


def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

def re_sub_repl_func():
    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))



def re_compile():
    pattern = re.compile(r'\d+') # 匹配至少一个数字
    m = pattern.match('one12twothree34four')
    print(m)

    m = pattern.match('one12twothree34four',2,10)
    print(m)

    m = pattern.match('one12twothree34four',3,10)
    print(m)
    print(m.group(), m.start(), m.end(), m.span(),sep='\t')

    # exmaple 2
    pattern = re.compile(r'([a-z]+) ([A-Z]+)', re.I)

    m = pattern.match('Hello World Wide Web')
    print(m)

    print(m.group(), m.group(1), m.group(2), sep='\t')
    print(m.span(), m.span(1), m.span(2), sep='\t')


def sub_print(matched):
    value = matched.group('value')
    print(value)


def re_findall():
    '''
    找到数字
    '''
    # 方法1 可行 --- findall
    raw = 'runoob 123 google 456'
    result1 = re.findall(r'\d+',raw)
    print(result1)

    # 方法2 不可行 --- search 只会找第一个匹配, 而match只招开头，且只匹配一次
    matchObj = re.search(r'\d+',raw)
    if matchObj:
        print(matchObj.group())

    # 方法3 不可行 --- sub 会找所有匹配，但是要repl
    new = re.sub(r'\d+','', raw)
    print(new)

    # 方法4 可行--- sub repl函数输出match
    new = re.sub(r'(?P<value>\d+)', sub_print, raw)

    # 方法5 可行 --- findall， compile
    pattern = re.compile(r'\d+')
    result2 = pattern.findall(raw)
    print(result2) 

    result2 = pattern.findall(raw,0,10)
    print(result2) 

    result2 = pattern.findall(raw,12,20)
    print(result2) 


if __name__=='__main__':
    # re_match()

    # re_search()

    # re_sub()

    # re_sub_repl_func()

    # re_compile()

    re_findall()