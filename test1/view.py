# -*-coding:utf-8 -*-
import os
import uuid
from flask import   session, request,Module
from flask_session import Session
# view = Flask(__name__)
view =Module(__name__)

sess = Session()

view.debug = True
view.secret_key = 'xxxx'

view.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
view.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
# view.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀


Session(view)

@view.route("/login")
def login():

    param =request.form if request.method=='POST' else request.args
    username = param.get("name")
    password = param.get("password")
    code = param.get("checkcode")

    ckeckcode = session["checkCode"]

    return  (username+password) if code == ckeckcode else ("checkCode is error ")

    return "sssss"


@view.route("/index")
@view.route("/home")
def index():
    try:

        # checkcode = random.randint(1000)
        checkcode = str(uuid.uuid1())
        print(checkcode)
        session["checkCode"] = checkcode
        return "<form action='/login'><input name = 'name'></br>" \
               "        <input type ='password' name = 'password'></br>" \
               "<input  name = 'checkcode'>" + checkcode + "</br>" \
                "<input type='submit' value = 'commit'>提交</input>"\
               "</form>"
    except Exception, e:
        print(e)
        return "error:           "+str(e)

if __name__ == '__main__':
    view.secret_key = 'super secret key'
    view.config['SESSION_TYPE'] = 'filesystem'

    sess.init_view(view)

    view.debug = True
    from werkzeug.contrib.fixers import ProxyFix
    view.wsgi_view = ProxyFix(view.wsgi_view)
    view.run(port=5001)