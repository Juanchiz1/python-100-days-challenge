

print("WELCOME TO THE CALCULATOR!!!")

def add(n1,n2):
    """Sum two numbers"""
    return n1+n2

#TODO-1 Write the other 3 functions - substract,multiply and divide:

def subtract(n1,n2):
    """Subtract two numbers"""
    return n1-n2

def multiply(n1,n2):
    """Multiply two numbers"""
    return n1*n2

def divide(n1,n2):
    """Divide two numbers"""
    return n1/n2

#TODO-2 Add these 4 functions into a dictionary as the values. KEYS="+","-","*","/"

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

resultadoGeneral=0

#TODO-3 Use the dictionary operations to perfom the calculations, multiply 4*8 using the dictionary
continuar="YES"
continuar2="YES"
n1=0
executed=False
while continuar=="YES":
    result=0
    if executed==False:
        n1=float(input("Enter the first number: \n "))
    else:
        n1=resultadoGeneral
        print("The stored result is:",n1, "and will be used as number #1")
    operator=input("Enter the operator: + , - , * , / ")
    n2=float(input("Enter the second number: \n "))
    for op in operations:
        if operator==op:
            result+=operations[op](n1,n2)
        else:
            continue
        break
    print(f"The result of {n1} {op} {n2} is: ", result)
    continuar2=input("Want to Continue making operations with the result?: YES OR NO \n").upper()
    resultadoGeneral += result
    executed=True
    if continuar2=="NO":
        if(continuar2=="NO"):
           resultadoGeneral=0
           executed=False

        continuar = input("Want to continue making operations?: YES OR NO \n").upper()


