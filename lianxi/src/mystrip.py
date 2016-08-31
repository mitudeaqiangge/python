#!/usr/bin/python
#-*-coding:utf-8-*-
#mystrip
import sys , os
s = ")(*&^hello jeapedu.com!@#$$%%"
d= "@)#$(*&!^%"
h= 0 
e = 0
i = 0
while i < len(s):
    if s[i] not in d:
        h = i
        break
    i += 1
print s[h:]
i = len(s) - 1
while i >= 0:
    if s[i] not in d:
        e = i + 1
        break
    i -= 1
print s[:e]
