#!/usr/bin env python
#-*-coding:utf-8-*-
import os, sys ,socket
s = socket.socket()
host = socket.gethostname()
port = 1234
#while True:
s.connect((host,port))
print s.recv(1024)
