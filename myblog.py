#-*- coding: utf-8 -*-

from flask import abort
from flask import Flask
from flask import make_response
from flask import redirect
from flask import request
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response("<h1>It's Adai's Blog!</h1><p>Your Browser is %s!</p>" % user_agent)
    response.set_cookie('answer', '42')
    return response


@app.route('/other')
def other():
    return redirect("http://www.baidu.com")


@app.route('/user/<name>')
def user(name):
    return "<h1>It's Adai's Blog! Welcome %s!</h1>" % name


# @app.route('/user/id/<id>')
# @login_required
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return "<h1>It's Adai's Blog! Welcome %s!</h1>" % user.name


if __name__ == '__main__':
    manager.run()
