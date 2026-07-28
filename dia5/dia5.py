#Listas
fruits=["Apples","Strawberries","Pears"]

#Bucles
for fruit in fruits:
    print(fruit)
    print(fruit+"pie")

student_scores=[150,142,232,123,456,120,100,80,45,65,120,125,135]

total=sum(student_scores)

print(total)

sum=0
for score in student_scores:
    sum=sum+score
print(sum)


max=0
for score in student_scores:
    if score>max:
        max=score
print(max)

#Range
for number in range(1,11,2):
    print(number)


sum2=0

for number in range(1,101):
    sum2=sum2+number
print(sum2)