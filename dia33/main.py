import datetime

import requests


response=requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data=response.json()

longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]

iss_possition=(latitude,longitude)
print(iss_possition)

parameters={"lat":latitude,"lng":longitude,"formatted":0}
response2=requests.get(url="http://api.sunrise-sunset.org/json",params=parameters)
response2.raise_for_status()
data2=response2.json()
sunrise=data2["sunrise"]
sunset=data2["sunset"]

time_now=datetime.datetime.now()
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
print(time_now.hour,time_now.minute,time_now.second)


