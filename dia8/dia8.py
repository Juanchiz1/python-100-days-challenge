#Functions with Inputs


def greet(name):
    print(f"Hello {name}")

greet("Juan")

#Functions with more than 1 input

def greet_with(name,location):
    print(f"Hello {name} From {location}")

greet_with("Juan","Colombia")

def greet_with(name="martin",location="Canada"):
    print(f"Hello {name} From {location}")

greet_with()