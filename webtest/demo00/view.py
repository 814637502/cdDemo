# coding:utf-8
from flask import jsonify
from webtest.demo00 import demo00  #蓝图的注册放在init里面

@demo00.route("/")
def demo():
    return jsonify(name="林妹妹")


