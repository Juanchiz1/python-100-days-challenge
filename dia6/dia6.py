print("Hello")
num_char=len("Hello")
print(num_char)

#create our own functions

def my_function():
    print("Hello")
    print("Bye")

my_function()


#for loop

def jump():
    print("Saltando")

number_of_hurdles=6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles-=1
    print(number_of_hurdles)