# coding:utf-8
from cmd import Cmd

__author__ = 'sunyawei'
import os

__author__ = 'root'
def cmd(cmds):
    os.system(cmds)
    print(__doc__)

    while 1:
        cmds = raw_input("commond::/")
        print(str(cmds))
        cmd(str(cmds))

'''第二种cmd的方法  自定义cmd'''
class CmdInterface(Cmd):
    def do_say_hello(self, argc):
        print "hello! " + argc
if __name__ == "__main__":
    welcome = "welcome a simple command interface demo demo"
    CmdInterface().cmdloop(welcome)