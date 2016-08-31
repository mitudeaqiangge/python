#-*-coding:utf-8 -*-
import math
import random
#打印jeapedu000~jeapedu100
i = 0
while i <= 100:
    if i < 10:
        print "jeapedu00" + str(i)
    elif i < 100 :
        print "jeapedu0" + str(i)
    else:
        print "jeapedu" + str(i)
    i += 1
i = 0
while i < 20:
    x = random.randint(1000000,10000000)
    s = str(x)
    if "4" in s and "7" in s:
        print "has 4 and 7 ",s
        if "6" in s or "8" in s:
            print "has 6 or 8 in " ,s
    else:
        print "has 4 and 7",s
    i += 1

x = 97
print chr(x)
i = 0
while i < 26 :
    s = chr(x+i)
    print s+str(i+1),
    i += 1
    




    
    
    
    
    
    
      

