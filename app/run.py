# coding:utf-8
import os
from app import app
from setting import Config
__author__ = 'sunyawei'

from app import app
from webtest.demo00 import view
'''' 测试   __import__
    想要通过__import__动态导入其他包，没成功
'''''
if __name__ == '__main__':
    files = Config.FileModule
    for file_name in files:
        for modual_name in files[file_name]:
            modual = __import__('webtest.demo01.view')
            demo00 = modual.demo00
            print("name  =  " + modual.demo00.__name__ + "  " + demo00.__name__)
            print(demo00.demo00)

            # app.register_blueprint(modual, url_prefix=('/'+modual_name))
    # for file_name in fileList:
    #     if os._isdir(file_name)
    #     print(file_name)
    # webtest.demo01.view
    demo00a = __import__("webtest.demo00.view")
    # print(demo00a.__name__)
    # print(demo00a.demo01)
    # app.register_blueprint(demo00, url_prefix='/user')
    # app.register_blueprint(demo01, url_prefix='/demo01')



    # app.run()