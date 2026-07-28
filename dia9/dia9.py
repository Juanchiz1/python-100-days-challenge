#Dictionaries in Python

programmingDictionary={"Bug":"An error in a program",
                       "Function":"A piece of code that you can easily call over and over again",
                       "Loop": "The action of doing something over and over again"}

print(programmingDictionary["Bug"])

programmingDictionary["HTML"]="Web Programming Language"
print(programmingDictionary["HTML"])

programmingDictionary["Bug"]="Hello"

for thing in programmingDictionary:
    print(programmingDictionary[thing])

capitals={
    "France":"Paris",
    "United Kingdom":"London",
    "Germany":"Berlin",

}

travel_log={
    "France":["Paris","Little","Dijon"],
    "Spain":["Madrid","Catalonia","Seville"],
    "Berlin":{
        "Bavaria":["Hannover","Lidia"],
        "Prussia":"Hellas"
    }
}

print(travel_log["Spain"][0])

nested_list=[1,2,["C","D"]]
print(nested_list[2][0])

print(travel_log["Berlin"]["Bavaria"][1])

