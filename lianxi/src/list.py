#-*-coding:utf-8-*-
li1 = range(2,8)
li2 = range(9,15)
print li1
print li2
p5 = li1.index(5)
print 5
li1.insert(p5,li2[len(li2)-1])
print li1
i = len(li2) -1
while i >= 0:
    print i,li2[i]
    li1.insert(p5,li2[i])
    print li1
    i -= 1
# 用append实现extend
i = 0 
while i < len(li2):
    v=li2[i]
    li1.append(v)
    print li1
li = [1,2,1,3,3,4,2,1,3,4,5,64,2] 
print li
i = 0 
while i < len(li):
    print li[i]
    if li[i] == 2:
        print 'pop 2' ,li.pop(i)
        i -= 1
    i += 1   
    
     
    
    
    
    
    
    







   
