import csv
import pandas as pd
from numpy.ma.extras import average

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1]=="temp":
            pass
        else:
            temperatures.append(int(row[1]))
print(temperatures)

datos=pd.read_csv("weather_data.csv")
#print(type(datos))
#print(datos["temp"])

datos_dict=datos.to_dict()
print(datos_dict)

datos_list=datos["temp"].to_list()
print(datos_list)

mean=average(datos_list)
print(mean)

maximo=datos["temp"].max()
datos_list.remove(maximo)
print(datos_list)

#get data from the rows
print(datos[datos.day=="Monday"])
print(datos[datos.temp==datos.temp.max()])

monday=datos[datos.day=="Monday"]
monday_temp=monday.temp[0]
monday_temp_f=monday_temp*9/5+32
print(monday_temp_f)

data_dict={
    "Students":["Amy","James","Angela"],
    "scores":[4.5,5,3.4]
}
dato_estudiante=pd.DataFrame(data_dict)
print(dato_estudiante)
dato_estudiante.to_csv("estudiante.csv")