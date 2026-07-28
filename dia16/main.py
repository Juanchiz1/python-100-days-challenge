# import turtle
#
# timmy=turtle.Turtle()
#
# print(timmy)
#
# my_screen= turtle.Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.speed(1)
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()



from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
menu.drink=drink = ""
while drink!="off":
    print("Welcome to the coffee machine!")
    options=menu.get_items()
    drink=input(f"Which drink would you like to make? {options}")

    if (drink == "report"):
        CoffeeMaker.report(coffee_maker)
        money_machine.report()
        break
    if (drink == "off"):
        print("Turning OFF!!")
        break
    else:
        drink2=menu.find_drink(drink)
        sufficient=coffee_maker.is_resource_sufficient(drink2)
        if sufficient:
            if money_machine.make_payment(drink2.cost):
                coffee_maker.make_coffee(drink2)





