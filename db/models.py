from sqlalchemy import Column, Integer, String, JSON, DateTime, func

__author__ = 'sunyawei'

from sqlalchemy.ext.declarative import declarative_base
    # 创建对象的基类
base = declarative_base()


class TbTask(base):

    __tablename__ = "tb_task"

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(128), index=True, unique=True, nullable=False)
    content = Column('content', JSON, nullable=True)
    user_id = Column('user_id', Integer, nullable=True)
    attach_list = Column('attach_list', String(1000), nullable=True)
    create_time = Column('create_time', DateTime, nullable=True, default=func.now())
    update_time = Column('update_time', DateTime, nullable=True, default=func.now(), onupdate=func.now())

    def __init__(self, id=None, name=None, content=None, user_id=None, attach_list=None,
                 create_time=None, update_time=None):
        self.id = id
        self.name = name
        self.content = content
        self.user_id = user_id
        self.attach_list = attach_list
        self.create_time = create_time
        self.update_time = update_time

