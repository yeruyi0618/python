# coding=utf-8
a = input('please enter a number: ')
if a < 10:
    print ('a<10')
elif a == 10:
    print ('a=10')
else:
    print ('a>10')

# for 循环
for i in range(1,11):
    print ('富婆走的第{}天，想他'.format(i))
'''
#while 循环
a=1
while a<=10:
    print (a)
    a=a+1

#break  条件满足就停止循环
for i in range(1,11):
    if i == 5:
        break
    print (i)
#continue   跳过条件符合继续循环
for i in range(1,11):
    if i == 5:
        continue
    print (i)
'''
