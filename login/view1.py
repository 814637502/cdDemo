__author__ = 'sunyawei'



blog = module(__name__)
@blog.route('/')
def index():
    return "This is my blog!"
@blog.route('/article/<int:id>')
def article(id):
    return "The article id is %d." % id