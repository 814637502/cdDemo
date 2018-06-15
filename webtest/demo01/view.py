# coding:utf-8
from flask import Blueprint, jsonify

__author__ = 'sunyawei'

demo01 = Blueprint("demo01", __name__)


@demo01.route("/")
def demo():
    return jsonify(name="小鬼哥")

print("super.__name__======"+super.__name__)