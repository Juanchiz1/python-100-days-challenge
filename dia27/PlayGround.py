
def add(*args):
    result=0
    for arg in args:
       result= sum(args)
    return result


print(add(4,5,1,5))

def calculate(n,**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5)


class Car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]
        self.color=kw.get("color",None)
        self.speed=kw.get("speed",None)

my_car=Car(make="Ford",model="Mustang",color="blue")
print(my_car.make)
print(my_car.model)
print(my_car.color)