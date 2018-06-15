# coding:utf-8
__author__ = 'sunyawei'

# def demo00():
#     aa = 1
#     def demo():
#         nonlocal aa
#         aa += 1
#         print(aa)
#
# demo()

def demo02(list = []):
    list.append(11)
    return list

print(demo02());
print(demo02());
print(demo02());
print(demo02());
print(demo02());


def demo03():
    # 这两种写法会有不同的结果  元组 VS  int
    s = (1)
    s1 = (1,)
    # 这两种写法会有不同的结果  元组 VS  str     就一个逗号的差别
    s0 = ("s0")
    s01 = ("s0",)
    print(type(s),type(s1))
    print(type(s0),type(s01))
demo03()
