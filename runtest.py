import os
from flask import  Flask
__author__ = 'sunyawei'

def run():
    flask_app = Flask(__name__)


    flask_app.register_module('D:/pycharm/workspace/demo5-8/login/view', url_prefix='/test')
    flask_app.secret_key = os.urandom(24)
    flask_app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run()