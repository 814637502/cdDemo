# coding:utf-8
import time
import datetime
# 获取当前的时间戳，精确到秒
t = time.time()
print(t)
# 精确到毫秒
tsss = int(t*1000)
print(tsss)

# 毫秒级时间戳转化为时间字符串
print("========================毫秒级时间戳转化为时间字符串=================================")
print(tsss)
tt = time.localtime(tsss*0.001)
print(time.strftime("%Y-%m-%d %H:%M:%S", tt))

# 时间字符串转为时间
print("==================================时间字符串转 datetime.datetime============================================")
strTimes = "2018-05-28 16:04:08"
strTimes = time.strftime("%Y-%m-%d %H:%M:%S", tt)
print(strTimes),
print(type(strTimes))
times = datetime.datetime.strptime(strTimes, "%Y-%m-%d %H:%M:%S")
print("转换为时间 "  )
print(times),
print(type(times))
print("==================================datetime.datetime  转  时间戳============================================")
print(times.timetuple())
time_s = (time.mktime(times.timetuple()))
print(time_s)

print("================================== 时间戳  转 datetime.datetime============================================")
# 1527501990315
# 2018-05-28 18:06:30
t = 1527501990315*0.001
print(datetime.datetime.fromtimestamp(t))
