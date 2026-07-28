

resources={
    "WATER":300,
    "MILK":250,
    "COFEE":100,
    "MONEY":0
}

drinks={
    "ESPRESSO":[50,18,0,1.5],
    "LATTE":[200,24,150,2.5],
    "CAPUCCINO":[250,24,100,3]
}

coins={
    "QUARTERS":0.25,
    "NICKLES":0.05,
    "PENNIES":0.01
}


drink=""
recursos=[]
bebidaRecursos=[]
UserMoney=0
llego=False


def report(resources):
    print("CURRENT RESOURCES: ")
    for r in resources:
        print(r)
        print("\t",resources[r])

def enoughResources(resources,drink,llego):
    UserMoney = processCoins()
    for d in drinks:
        if drink==d:
           bebidaRecursos=drinks[d]
        else:
            print("Drink doesn't exist")
            break

    for r in resources:
        recursos.append(resources[r])

    for i in range(0,len(bebidaRecursos)):
        if recursos[i]<bebidaRecursos[i]:
            if i==0:
                print("Sorry There is no enough water ")
                break
            elif i==1:
                print("Sorry There is no enough milk ")
                break
            elif i==2:
                print("Sorry There is no enough coffee ")
                break
            elif UserMoney<bebidaRecursos[3]:
                print(f"Sorry That is not enough money ${UserMoney} refunded ")
                break

            else:
                llego = True
    if llego:
        resources['WATER']-=bebidaRecursos[0]
        resources['MILK']-=bebidaRecursos[1]
        resources['COFEE']-=bebidaRecursos[2]
        cambio=UserMoney-bebidaRecursos[3]
        resources['MONEY']+=UserMoney-cambio
        if cambio>0:
            print(f"Here is your change ${cambio}")
        print(f"Enjoy your {drink} ")






def processCoins():
    quarters=numquarters*0.25
    nickles=numnickles*0.05
    pennies=numpennies*0.01
    UserMoney=quarters+nickles+pennies
    return UserMoney





while drink!="OFF":
    print("Welcome to the coffee machine!")
    drink=input("What would you like? (Espresso/Latte/Capuccino): ").upper()
    if(drink=="REPORT"):
        report(resources)
        break
    if(drink=="OFF"):
        print("Turning OFF!!")
        break
    print("Please Insert Coins!!: ")
    numquarters=int(input("How many quarters: "))
    numnickles=int(input("How many nickles: "))
    numpennies=int(input("How many pennies: "))
    enoughResources(resources, drink,llego)



