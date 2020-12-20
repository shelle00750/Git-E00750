from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/super_siple')
def super_simple():
    return '<h1>Hello from the Planetray API.</h1>'


if __name__ == '__main__':
    app.run()
