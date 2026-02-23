from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'
    return 'my python fisrt applicaiton'

if __name__ == '__main__':
    app.run()

