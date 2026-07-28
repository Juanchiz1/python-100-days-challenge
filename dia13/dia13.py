def my_function():
    for i in range(1,21):
        if i==20:
            print("You got it!!")

my_function()

try:
    age=int(input("Enter your age: "))
except ValueError:
    print("Sorry, you didn't enter a number.")
    age=input("Enter your age: ")

if age>18:
    print(f"you can drive at {age}.")