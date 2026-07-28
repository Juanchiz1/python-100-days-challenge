from tokenize import String

print("Welcome to the roallercoaster!!")
height=int(input("How tall are you in cm? "))
bill=0


if height>=120:
    print("You can ride the roallercoaster!!!")
    age = int(input("How old are you? "))
    if age>18 and age<45:
      bill=12
      print("Your tickets cost $12 Dollars")
    elif age<=12 or age<=18:
      bill=7
      print("Your tickets cost $7 Dollars")
    elif age>=45 or age<=55:
        bill=0
        print("Your tickets cost $0 Dollars")

    else:
        bill=5
        print("Your tickets cost $5 Dollars")
    Wantsphoto=input("Do you want photo? (Y/N): ")
    if Wantsphoto=="y" or Wantsphoto=="Y":
         bill+=3
         print(f"You have to pay {bill} Dollars")
    elif Wantsphoto=="n" or Wantsphoto=="N":
         print(f"You have to pay {bill} Dollars")
else:
    print("Sorry you have to grow taller before you can ride the roallercoaster!!!")

#modulo operator

#Even Number 12/2==0 Odd Number

number=int(input("Enter a Number: "))
if number%2==0:
    print(f"Your number is even")
else:
    print(f"Your number is odd")