from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort


application = Flask(__name__)
application.config.from_pyfile("app.config")


def func(a,b,op):
    if op == 'sum':
        return a + b, 'a + b'
    if op == 'dif':
        return a - b, 'a - b'
    if op == 'pow':
        return a ** b, 'a ** b'
    if op == 'mul':
        return a * b, 'a * b'
    if op == 'dig':
        return a / b, 'a / b'
    return 'Используй: sum, dif, pow, mul, dig', ''
        
@application.route('/')
def index():
    a = request.args.get('a', default =None, type=int)
    b = request.args.get('b', default =None, type=int)
    op = request.args.get('op', default =None, type=str)
    result, formula = func(a,b,op)
    
    return render_template('index.html', formula=formula, result=result)



if __name__ == "__main__":
    application.run(host="0.0.0.0")
