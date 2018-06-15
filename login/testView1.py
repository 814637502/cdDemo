from flask import Flask

__author__ = 'sunyawei'
apps = Flask(__name__)

@apps.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    apps.run(port=5001)