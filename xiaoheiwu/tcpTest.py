# -*-coding:utf-8  -*-
# from ctypes import *
from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)
msvcrt.printf('ipconfig')











