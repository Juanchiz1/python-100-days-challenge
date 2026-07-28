import pandas as pd

datos=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

pelo=datos["Primary Fur Color"]
numGray=0
numRed=0
numBlack=0

for elemento in pelo:
    if elemento=="Gray":
        numGray+=1
    elif elemento=="Cinnamon":
        numRed+=1
    elif elemento=="Black":
        numBlack+=1

print(numGray,numRed,numBlack)

data={
    "FUR":[0,1,2],
    "COLOR":["Gray","Cinnamon","Black"],
    "COUNT":[numGray,numRed,numBlack]
}

data_pd=pd.DataFrame(data)
data_pd.to_csv("Squirrel_Count.csv",index=False)