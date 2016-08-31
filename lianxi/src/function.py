#!/usr/bin/env python
#-*-coding:utf-8-*-
def countSubstr(s,ch):
    c = 0
    i = 0
    while i < len(s):
        print s[i]
        if s[i] == ch:
            c += 1
        i = i + 1
    print c
    
s1 = "hello jeapedu.com"
cc = "e"
countSubstr(s1, cc)
    