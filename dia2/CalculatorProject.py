print("Welcome to the tip calculator!!")
bill=float(input("What was the total bill?\n"))
tip=int(input("How much tip would you like to give? 10, 12, or 15\n"))
people=int(input("How many people to split the bill?\n"))
porcentageTip=bill*tip/100
preTotal=bill+porcentageTip
total=round(preTotal/people,2)
print(f"Your total bill is {preTotal}")
print(f"Each person should pay {total}")