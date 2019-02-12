# coding:utf-8
__author__ = 'sunyawei'
# -*- encoding:utf-8 -*-
import calendar
# 设置每周的起始日期码,为星期天
calendar.setfirstweekday(firstweekday=6)
# 返回2019年年历
print(calendar.calendar(2019, w=2, l=1, c=6))