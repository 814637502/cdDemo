# -*-coding:utf-8 -*-
import uuid

__author__ = 'sunyawei'
from flask import Flask, session, request
from login.flask_session import Session
app = Flask(__name__)
sess = Session()

app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
# app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀


Session(app)

@app.route("/login")
def login():

    param =request.form if request.method=='POST' else request.args
    username = param.get("name")
    password = param.get("password")
    code = param.get("checkcode")

    ckeckcode = session["checkCode"]

    return  (username+password) if code == ckeckcode else ("checkCode is error ")

    return "sssss"


@app.route("/index")
@app.route("/home")
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
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(port=5001)