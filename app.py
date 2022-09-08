from flask import Flask, render_template, request


application = Flask(__name__)


@application.route('/')
def index():
    name = 'Username'
    return render_template('index.html', title='Welcome', username=name)


@application.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


if __name__ == "__main__":
    application.run(host="0.0.0.0")
