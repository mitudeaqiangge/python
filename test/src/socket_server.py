#!/usr/bin env python
#-*-coding:utf8-*-
import tab
import sys , os ,commands
#connect
#USER  PASSWD  HOST  Database
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5)
while True:
    c ,addr =s.accept()
    print "Got connect from ",addr
    c.send("Thank you for connect")
    c.send("address %s") %addr
    c.send("kkkkkkkkkkkk")
    c.close()
    