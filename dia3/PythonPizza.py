print("Welcome to Python Pizza Delieveries!!!")
size=input("What size pizza do you want? S, M or L")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Please enter a valid size")

pepperoni=input("Do you want pepperoni? Y or N").strip().upper()
if pepperoni=="Y"  and (size =="S"):
    bill+=2
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill+=3

extra_cheese=input("Do you want extra cheese? Y or N")
if extra_cheese=="Y" or extra_cheese=="y":
    bill+=1

print(f"Your Finall Bill is={bill}")
