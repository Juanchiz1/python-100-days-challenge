

print("Welcome to the Secret Auction Program!"
      "💵💵💵")
bid_Dictionary={}
continuar="yes"
actual=0
nombre=""

while continuar=="yes":
    name=input("What is your name?  ")
    bid=int(input("What is your bid? $ "))
    bid_Dictionary[name]=bid

    continuar=input("Want to Continue?: YES OR NO \n").lower()
    print("\n" * 5)

for key in bid_Dictionary:
    if bid_Dictionary[key]>actual:
        nombre=key
        actual=bid_Dictionary[key]
print(f"The biggets bid was {actual}💲 made by {nombre}. 🪙")

