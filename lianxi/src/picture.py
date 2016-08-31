#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib
import urllib2
import sys
url1 = raw_input("url: ")
up1 = urllib2.urlopen(url1)
s1=up1.read()
#print s
h1 = "<a href="
c1 = ".html"
posh1 = -len(h1)
posc1 = -len(c1)
j = 0 
while j < s1.count(h1):
    posh = s1.find(h1,posc1 +len(h1))
    posc = s1.find(c1,posh1 +len(h1))
    t1 = s1[posh1 : posc1 + len(c1)]
    print t1
    http1 = t1.find("/tupianqu")
    print http1
    #if len(t[http:]) == len(temp):
    url = "http://1122ap" + t1[http1:]
    print url

    up = urllib2.urlopen(url)
    s=up.read()
    #print s
    h = "<img src="
    c = ".jpg"
    temp = ""
    posh = -len(h)
    posc = -len(c)
    i = 0 
    while i < s.count(h):
        posh = s.find(h,posc +len(h))
        posc = s.find(c,posh +len(h))
        t = s[posh : posc + len(c)]
        http = t.find("http")
    #print http
    #if len(t[http:]) == len(temp):
        url = t[http:]
        print url
        try:
            urllib.urlretrieve(url,str(i) + 'jpg')
            print "picture from %s ;download sucessful" % url
        except:
                print "Unexpected error:", sys.exc_info()[0]
        i += 1
    j += 1
        
        
    
