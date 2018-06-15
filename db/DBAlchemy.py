# coding:utf-8
# from db.models import TbTask

__author__ = 'sunyawei'

from sqlalchemy import column,String,create_engine, Column, Integer, JSON, DateTime, func
from  sqlalchemy.orm import sessionmaker

def get_db():
    # from sqlalchemy.ext.declarative import  declarative_base
    # 创建对象的基类
    # base = declarative_base()
    # 初始化数据库连接
    engine = create_engine("postgresql://postgres:postgres@10.95.134.21:62432/situation")
    # 创建DBsession类型
    DBsession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBsession()
    return session
# a = session.execute("select id,name,CREATE_time,update_time from tb_task")
# for aa in a:
#     print(aa)
session = get_db()
# a = session.query(TbTask).all()

aa = A
print(aa.getss())
# for aa in a:
#     print(aa)
print("=========================================")