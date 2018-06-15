__author__ = 'sunyawei'

import threading

def getc(l = []):
    l.append([])
    return len(l)
def sayhello():
    print "hello world",
    global t #Notice: use global variable!
    print(getc())
    t = threading.Timer(0.01, sayhello)
    t.start()


t = threading.Timer(0.01, sayhello)
t.start()