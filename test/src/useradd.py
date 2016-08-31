#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys , os ,commands
import pwd
global users
def useradd():
    while True:
        global users
        users=raw_input("请输入用户名:").strip()
        os.environ['user']=str(users)
        if commands.getstatusoutput('id -u $user >/dev/null 2>&1')[0] !=0 :
            os.system("sudo useradd  -d /home/$user $user ")
            print  "New user %s add success" %users
            break
        else:
            print "User name already exists. Please re-enter."
            continue
#def group():
    while True:
#        global users
        groups=raw_input("请输入一个用户所属组：").strip()
        os.environ['group']=str(groups)
 #       os.environ['user']=str(useradd.users)
        if commands.getoutput("sudo groups $group >/dev/null 2>&1"):
            os.system("sudo gpasswd -a $user $group ")
            print "%s join group %s Success" %(users ,groups)
            break
        else:
            os.system("sudo groupadd $group && gpasswd -a $user $group")
            print "%s join group %s Success" %(users,groups)
            break
#def passwd():
    pwd=raw_input("请输入用户密码：").strip()
#read -p "Please enter a user passwd:" pwd
#    os.environ['user']=str(useradd.users)
    os.system("echo $pwd | passwd --stdin $user")

while True:
    yn=raw_input("Do you wish to continue ... yes|no [yes]")
    if yn in ['y','Y','yes','YES','Yes']:
        useradd()
#        group()
#        passwd()
    elif yn in ['n','N','no','NO','No'] :
        break
    else :
        print "Please answer y or n."
if __name__ == '__main__':
    pass

    