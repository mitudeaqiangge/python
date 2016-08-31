#!/usr/bin/env python
#-*- coding:utf-8-*-
#python if test
#for i in range(101):
#    print i
s = "F"
i = 0
c = "r"
if s != "M" and c == "r":
    i = i+10
    print "Gentlenmen"
else:
    print "lady"
print "end"
rec = 88
if rec >= 90 or rec <=100:
    print "Best"
if rec >=80 and rec <= 90:
    print "Better"
if rec < 60 :
    print "your should imporove"

record = int(raw_input("your record:"))
if record >= 60:
    if record >=70:
        if record >= 80:
            if record >= 90:
                print "A"
            else:
                print "b"
        else:
            print "c"
    else:
        print "D"
    print "pass"
else:
    print "不及格"







