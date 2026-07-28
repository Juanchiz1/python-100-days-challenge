import random
from random import choice

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
symbols=['!','#','$','&','/','(','?','*','+','-']

print("Welcome to PasswordGenerator!!")
letter=int(input("How Many Letters Do You Want in your password?: \n"))
number=int(input("How Many Numbers Do You Want in your password?: \n"))
symbol=int(input("How Many Symbols Do You Want in your password?: \n"))

letterChosen=[]
i=0


while i<=letter-1:
    range = random.randint(0, 24)
    letterChosen.append(letters[range])
    i+=1

numberChoosen=[]
i=0

while i<=number-1:
    range = random.randint(0, 24)
    numberChoosen.append(numbers[range])
    i+=1

symbolChosen=[]
i=0

while i<=symbol-1:
    range = random.randint(0, 9)
    symbolChosen.append(symbols[range])
    i+=1

prePassword=[]
rango=letter+number+symbol
password = []
i=0

while i<(rango/3):
    prePassword.append(random.choice(letterChosen))
    prePassword.append(random.choice(numberChoosen))

    prePassword.append(random.choice(symbolChosen))
    i+=1

print(f"Your Password is: {prePassword}")


