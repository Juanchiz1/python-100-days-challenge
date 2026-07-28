import random

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_list=[item+1 for item in numbers]

print(new_list)

name="Juan"

new_name=[letter for letter in name]
print(new_name)

rango=range(1,5)

new_rango=[r*2 for r in rango]
print(new_rango)

names=["JUAN","DIEGO","alexa","MARÍA","ALEJANDRA","ORIANA"]

short_names=[name for name in names if len(name)<=5]
print(short_names)

upper_names=[name.upper() for name in names if name.islower()]
print(upper_names)

students={student:random.randint(0,5) for student in names}
print(students)

passed_students={student:value for (student,value) in students.items() if value>=3}
print(passed_students)

import pandas as pd

student_dict={
    "student":["Angela","Juan","Orlando","Matías"],
    "score":[4,3,2,5]
}
students_data=pd.DataFrame(student_dict)
print(students_data)

for (index,row) in students_data.iterrows():
    print(row.student)