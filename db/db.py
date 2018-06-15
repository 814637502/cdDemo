# coding:utf-8
import StringIO
from openpyxl import workbook
import xlwt

__author__ = 'sunyawei'
import psycopg2
def get_db():
    conn = psycopg2.connect(database="situation", user="postgres", password="postgres", host="10.95.134.21", port="62432")
    print "Opened database successfully"
    conn = conn.cursor()
    '''我想直接查处来列名 执行不了'''
    # sql = '''select *  from information_schema.columns '''
    # columns = conn.execute(sql)
    # print(columns)
    conn.execute('''select id,name,CREATE_time,update_time from tb_task''')

    rows = conn.fetchall()
    for row in rows:
            print row
            # print(type(row))
    conn.close()
# get_db()


def to_export():

    workbooks = xlwt.Workbook(u"玲妹妹")
    sheets = workbooks.add_sheet(u"xiaogui.xls", cell_overwrite_ok=True)
    sheets.write(0, 0, u"我是")

    workbooks.save("C:/Users/sunyawei/Desktop/a.xls")

    # column_map = {
    #     'name': {'column_name': 'A', 'column_title': u'姓名', 'width': 20},
    #     'id_card': {'column_name': 'B', 'column_title': u'身份证号', 'width': 20},
    #     'email': {'column_name': 'C', 'column_title': u'邮箱', 'width': 20},
    #     'mobile_phone': {'column_name': 'D', 'column_title': u'手机号码', 'width': 20},
    #     'position': {'column_name': 'E', 'column_title': u'职务', 'width': 20},
    #     'unit': {'column_name': 'F', 'column_title': u'单位', 'width': 20},
    #     'skills': {'column_name': 'G', 'column_title': u'技能', 'width': 20}
    # }

# 公司用的

import time
import datetime
import sched


# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedul = sched.scheduler(time.time, time.sleep)
start_time = 0
end_time = 0

class Mytimer(object):
    #被周期性出发的函数
    def excute_command(self,):
        print("sssssssssssssssssssss")
        pass

    def cmd_timer(self, cmd, time_str, inc=60):
        # cmd：windows中命令行代码
        # time_str：哪一个时间点开始第一次执行
        # inc：两次执行的间隔时间
        # enter四个参数分别为：间隔时间、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
        # 给该触发函数的参数（tuple形式）
        now = datetime.datetime.now()
        schedule_time = datetime.datetime.strptime(time_str, '%H:%M').replace(year=now.year, month=now.month, day=now.day)
        if schedule_time < now:
            schedule_time = schedule_time + datetime.timedelta(days=1)
        time_before_start = int(round((schedule_time-datetime.datetime.now()).total_seconds()))
        print u'mytimer => 还有%s秒开始任务' %time_before_start
        schedul.enter(time_before_start, 0, self.execute_command, (cmd, inc))
        schedul.run()
print("=====================================用这个可能导致主线程的锁被阻断了  建议用threadind的timer=============================================")
def dos():
    print("================================================")

now = datetime.datetime.now()
schedule_time = datetime.datetime.strptime("15:00", '%H:%M').replace(year=now.year, month=now.month, day=now.day)
print(schedule_time)
print(now)
if schedule_time < now:
    schedule_time = schedule_time + datetime.timedelta(days=1)
    print("schedule_time =  "),
    print(schedule_time)
else:
    print("start")
# 还有多久才执行执行这个任务
time_before_start = int(round((schedule_time-datetime.datetime.now()).total_seconds()))
print(time_before_start)
schedul.enter(10, 0, dos, ())
# schedul.run()

print("===================================== threadind的timer=============================================")
from  threading import _Timer

def doss():
    print("is doss ")
    # _Timer(1,doss,()).start()
_Timer(1,doss,()).start()
