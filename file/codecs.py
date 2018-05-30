# -*-coding:utf-8-*-
import codecs
# 操作文件的
__author__ = 'sunyawei'
#只写
fn2 = codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'w', "utf-8")
fn2.write('')
fn2.close()
print("读取前")
#读取文件
fn = codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'r+', "utf-8")
# line = [i.strip() for i in fn]
line = fn.read()
print(line)

# 在后边添加  追加元素
fn = codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'a+', "utf-8")
fn.write(u"\r\n你好呀aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw sw 你是谁？")
fn.close()

fn2 = codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'w', "utf-8")#清空
fn2.write('')
fn2.close()

def a():
    print("close--------------------")
def b():
    def __exit__():
        print(u"exit")
        pass

    print("open--------------------")

# fn  = codecs.open('C:/Users/sunyawei/Desktop/a.txt','a+', "utf-8")
codecs.close=a();

#默认调用的close方法
with codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'a+', "utf-8") as f:
    f.write(u'我是谁')
    f.write(u'我是谁')
    f.write(u'我是谁')
with codecs.open('C:/Users/sunyawei/Desktop/a.txt', 'r', "utf-8") as f:
    print(f.read())

with b() as aa:
    print("aa=")