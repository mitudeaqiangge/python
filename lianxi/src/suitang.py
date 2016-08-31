#-*-coding:utf-8-*-
#slice
b=['a','d','d']
#s=str(b)
s=b[0]+b[2]+b[2]
print b[0:1]

s = "http://www.wangmin.com http://chinaswift.com http://www.lianqiang.com"
h="http"
c=".com"
posh = -len(h)
posc= -len(c)
i = 0
while i < s.count(h):
    posh = s.find(h,posh+len(h))
    posc = s.find(c,posc+len(h))
    print posh,
    print posc, s[posh :posc+len(c) ]
    i += 1
    