# coding=utf-8
#逢7跳过

for i in range(1,101):
    if i%7 == 0 or i%10 == 7 or i//10 == 7:
        continue
    else:
        print (i)
    #elif i%10 == 7:
      #  print (i)


