import random
import my_module

random_integer=random.randint(1,10)
print(random_integer)

print(my_module.my_favorite_number)

#float random numbers

random_float=random.random()
print(random_float)

random_float2=random.uniform(10,20)
print(random_float2)

num1=random.randint(0,5)
num2=random.randint(6,10)

if num1==0 or num1>=5 :
    print("Heads")
elif num2==6 or num2<=10:
    print("Tails")    
