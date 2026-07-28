import random


def guesses(attempts):
    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == numero:
            print("You got it! the number was " + str(numero))
            break
        elif guess > numero:
            attempts = attempts - 1
            print("To high \n Guess again!")
            print("You have " + str(attempts) + " attempts left to guess the number.")
        elif guess < numero:
            attempts = attempts - 1
            print("To low \n Guess again!")
            print("You have " + str(attempts) + " attempts left to guess the number.")
    print(f"You have lost the number was {numero} try again!")


print("Welcome to the Number Guessing Game!")
numero=random.randint(1,100)
print("I am thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty level:  'easy' or 'hard': ").upper()
attempts=0

if difficulty=="EASY":
    attempts=10
    print(f"You have {attempts} attempts left to guess the number.")
    guesses(attempts)
elif difficulty=="HARD":
    attempts=5
    print(f"You have {attempts} attempts left to guess the number.")
    guesses(attempts)
else:
    print("Invalid difficulty level")






