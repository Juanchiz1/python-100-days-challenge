from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"\
        "<p>Welcome to my Flask app!</p>"\
        "<img src='https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif' alt='Hello GIF'>"    

@app.route('/bye')
def say_bye():
    return '<h1>Goodbye, World!</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello there, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)

