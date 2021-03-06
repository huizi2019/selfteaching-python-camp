text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''

dict1 = {} #设立数据容器
dict2 = {}
dict3 = {}
dict4 = {}

def stats_text(text):  #设定合并词频函数
    if not isinstance(text,str):
        raise ValueError('输入参数不为字符串类型')
    return dict(stats_text_en(text),**stats_text_cn(text))


def stats_text_en(text):  #设定函数
    if not isinstance(text,str):
        raise ValueError('输入参数不为字符串类型')
    import re  #引入系统函数
    
    text = re.sub("[^A-Za-z]", " ", text.strip()) #只留英语单词
    
    list1 = re.split(r"\W+",text)   #把单词存入一个list里
    
    while '' in list1:   
        list1.remove('')  #删除空格
    
    for i in list1:   
        
        dict1.setdefault(i,list1.count(i))  #把单词及其频次统计到一个字典里
    
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #按照字频排序
    
    for tup1 in tup1:   #历遍元组tup1
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2  #组装到新字典中


    stats_text(text)
    


def histogram(s, old_d): #设置一个更新数量的函数
    
    d = old_d
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
    

def stats_text_cn(text): #只针对汉字的函数
    if not isinstance(text,str):
        raise ValueError('输入参数不为字符串类型')
    import re
    
    text = re.sub("[A-Za-z0-9]", "", text) #遴选出汉字
    
    list1 = re.split(r"\W+",text)   #分割汉字

    
    while '' in list1:   
        list1.remove('') #去除空格

    
    dict3 = dict()  #use dict function
    
    for i in range(len(list1)): 
        dict3 = histogram(list1[i], dict3)

    
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

    
    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

    stats_text(text)


#print(stats_text(text)) #打印合并词频结果





    



