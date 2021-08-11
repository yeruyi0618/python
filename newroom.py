# coding=utf-8
from __future__ import division #For decimal division
# format用法

template='hello {}, hello {}, hello {}'
beijing='Beijing'
china='China'
world='World'
result=template.format(beijing,china,world)
print(result)

#python的字符串编码
s1='我爱中国'
s2='wo ai zhong guo'
s3=13202003500
s4='!@#$$$4'

print s1,'\n',s2,'\n',s3,'\n',s4

#if语句  else  elif
age=51
if age<=3:
    print ('婴幼儿')
elif 3<age<=6:
    print ('儿童')
elif 6<age<=14:
    print ('青少年')
elif 14<age<18:
    print ('未成年')
elif age==18:
    print ('正好成年')
elif 50>age>18:
    print ('中年人')
else:
    print ('老年人')

#python之for循环
L=[49,34,99,83,78]
sum=0
for i in L:
    sum += i

    print (sum)

#while 循环
s=1
l=1
while s<=10:
    l=s*l
    s=s+1
    print (l)

age=input('my age is :')
print (age)

#计算浮点数，保留小数
L = [2,7,8]
A = 0
for s in L:
    A += s
print (format(float(A)/float(3),'.2f'))

# 0-1000以内偶数之和
a = range(0,1001)
b = 0
for s in a:
    if s%2 == 0:
        b += s
print (b)

#嵌套循环
s1 = 'ABC'
s2 = '123'
s3 = 'xyz'
for a in s1:
    for b in s2:
        for c in s3:
            print (a+b+c)

#按一定规则访问list容器
num = 0
L = ['Alix',22,'Model',44,'True','False']
for s in L:
    num += 1
    if num % 2 != 0:
        continue
    print (s)

#按照索引访问list容器
L = ['Alix',22,'Model',44,'True','False']
print (L[0])
print (L[1])
print (L[2])

#按照倒叙访问list容器
L = ['Alix',22,'Model',44,'True','False']
print (L[-1])
print (L[-2])
print (L[-3])

#插入list容器，增加元素
names = ['Alix','Bob','David','Ellena']
names.append('Zero')    #append默认添加到list最后
print (names)
names.insert(3,'China')    #insert方法可以指定位置添加
print (names)
names.insert(5,'Gen')
print (names)
names.insert(6,'Phone')
print (names)

#删除list容器元素
L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
name = L.pop(2)    #pop方法括号内如果不填参数则默认删除最后一个元素；如果填写参数，则删除指定序号
print(L)
name = L.pop(2)
print(L)

#按照分数重新排序 班上某次考试，['Alice', 'Bob', 'Candy', 'David', 'Ellena'] 的成绩分别是 89, 72, 88, 79, 99
names = ['Alix','Bob','Candy','David','Ellena']
names.insert(0,'Ellena')    #把第一名插入第一的位置
L = names.pop()    #删除最后一个名字以免重复
L = names.pop(2)
names.append('Bob') #默认添加到最后一个元素
print (names)

#求3个长方体的表面积，长宽高分别是：1 2 3， 5 3 2，7 3 2
L = [[1,2,3],[5,3,2],[7,3,2]]
for s in L:
    l = s[0]
    w = s[1]
    h = s[2]
    result = l * w * 2 + l * h * 2 + w * h * 2
    print (result)

#tuple与list的作用
L = (0,1,2,3,4,5,6,7,8,9)
M = list(L)    #把元组切换成list
M = tuple(L)    #把list切换成元组 元组是固定不变的，每个元素都不可以改变，也不能往元组添加数据
L.count(1)    #返回元组里面总共出现次数
L.index(1)    #返回元组里面出现该值的位置编码
print (M)

#两个list表一一对应打印
names = ['Alix','Bob','David','Ellena']
result = [78,69,85,99]
a = 0
for name in names:
    res = result[a]
    print ('names = {},result = {}'.format(name,res))
    a = a + 1

#读取dict元素内容
d = {
    'Alice':45,
    'Bob':60,
    'Candy':75,
    'David':86,
    'Ellena':49,
    'Gaven':86
}

print (d.get('Alice'),d.get('Bob'),d.get('Candy'),d.get('Mimi'),d.get('David'))

