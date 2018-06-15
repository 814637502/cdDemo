# coding:utf-8
from functools import wraps
from flask import logging, jsonify, session

__author__ = 'sunyawei'

def try_exception(f):

    def catchException(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception, e:
            return e

    return


def exception_catch(f):
    # @wraps(f)
    def decorated_function(*args, **kwargs):
        # token = session.get('csrf_token', '')
        try:
            print("我是装饰器")
            f(*args, **kwargs)
            return decorated_function
        # except ShowError, e:
        #     return jsonify({'status': 500, 'message': e.message, 'token': token})
        except Exception, e:
            logging.error('catch exception: %s, function name : %s ' % (str(e), f.__name__), exc_info=1)
            return jsonify({'status': 500, 'message': u'服务器内部错误', 'token': token})
        finally:
            print("装饰结束")
    return decorated_function
'''''''''''''''''''''''''''''''''''''''自己的测试'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def decorate(f):
    """
    wraps(f)   作用就是为了将回调函数控制给f的方法，效果就是看调用改装饰器的方法的__name__是方法自己的  不加这个就变成do_task了
    """
    @wraps(f)
    def do_task():
        try:
            print("执行前")
            f()
            return do_task
        except Exception, e:
            print(str(Exception))
            return f
        finally:
            print("执行后")
    return do_task

@decorate
def test():
    print("我要来了")
    # raise IOError
    print("方法执行结束")

a = test()
print(a.__doc__)
print(a.__name__)