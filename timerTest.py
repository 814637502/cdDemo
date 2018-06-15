# coding:utf-8
import threading
import time
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
__author__ = 'sunyawei'

def get_db():
    # from sqlalchemy.ext.declarative import  declarative_base
    # 创建对象的基类
    # base = declarative_base()
    # 初始化数据库连接
    engine = create_engine("postgresql://postgres:postgres@10.95.134.21:62432/situation", poolclass=NullPool)
    # 创建DBsession类型
    DBsession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBsession()
    session2 = scoped_session(DBsession)
    print(id(session2))
    session2.remove()
    session.close()
    print(id(session2))
    print("========================================")
    a = session.execute("select id from tb_task")
    for aa in a:
      print(aa)

    a = session2.execute("select id from tb_task")
    for aa in a:
      print(aa)


    print(id(session))
    print(session.is_active)

    session.close_all()
    # session._remove_newly_deleted()
    print(id(session))
    # print(session.is_active)
    # print(session._is_clean())
    # a = session.execute("select id from tb_task")
    # for aa in a:
    #   print(aa)
    # return session
get_db()
def get_data():

    return

def data2File():

    return

def export_file():

    return
def sleepTime(datesss):
    now = datetime.datetime.now()
    #根据传过来的时间点转换为对应当天的时间
    datess = datetime.datetime.strptime( datesss, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
    if datess < now:
        datess += datetime.timedelta(days=1)
    return (datess-datetime.datetime.now()).total_seconds()

# 每天定点去执行方法
def doTask(datesss="15:00"):



    time_after_start = sleepTime(datesss)
    print("即将在     "),
    print(time_after_start),
    print("   秒后会执行方法")
    threading._sleep(time_after_start)
    global t
    t = threading._Timer(time_after_start, doTask(), [])
    t.start()
#
# now = datetime.datetime.now()
# schedule_time = datetime.datetime.strptime(time_str,'%H:%M').replace(year=now.year,month=now.month,day=now.day)
# if schedule_time < now:
#     schedule_time = schedule_time + datetime.timedelta(days=1)
# time_before_start = int(round((schedule_time-datetime.datetime.now()).total_seconds()))


# 设置程序入口
d  = "18:47"
t = threading.Timer(0, doTask, [d])
# t.start()
