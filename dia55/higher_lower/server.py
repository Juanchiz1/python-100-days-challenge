import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Hello GIF'>"
        
number=random.randint(0,9)

@app.route('/<int:guess>')            
def check_guess(guess):
    if guess < number:
        return "<h1 style='color: red;'>Too low, try again!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Hello GIF'>"
    elif guess > number:
        return "<h1 style='color: red;'>Too high, try again!</h1>"\
            "img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Hello GIF'>"
            
    else:
        return "<h1 style='color: green;'>You found me!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Hello GIF'>"
            
if __name__ == '__main__':
    app.run(debug=True)
            