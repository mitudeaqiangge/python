#!/usr/bin/python
#-*-coding:utf-8-*-
#http://1122ap.com/tupianqu/zipai/
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
print s1.count(h1)
j = 0 
while j < s1.count(h1):
    posh = s1.find(h1,posc1 +len(h1))
    posc = s1.find(c1,posh1 +len(h1))
    t1 = s1[posh1 : posc1 + len(c1)]
    #print t1
    http1 = t1.find("/tupianqu")
    #print http1
    #if len(t[http:]) == len(temp):
    url = "http://1122ap" + t1[http1:]
    #print url











