import requests
from datetime import datetime
pixela_end_point="https://pixe.la/v1/users"
TOKEN="<PASSWORD>"
USER_NAME="Juan Diego"
GRAPH_ID="GRAPH_ID"
user_params={
    "token":"rr43wss3",
    "username":"juanchiz",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response=requests.post(url=pixela_end_point,json=user_params)

graph_endpoint=f"{pixela_end_point}/{TOKEN}/graphs"

graph_config={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#response=requests.post(url=graph_endpoint, json=graph_config,headers=headers)
#print(response.text)

pixel_creation_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"

today=datetime.now()

pixel_data={
    "date":today.strftime("%Y-%m-%d"),
    "quantity":input("How Many Kilometers did you cycle today?: ")

}

#response=requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
#print(response.text)

update_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y-%m-%d')}"

new_pixel_data={
    "quantity":"4.74",
}

#response=requests.put(url=update_endpoint, headers=headers, json=new_pixel_data)
#print(response)

delete_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y-%m-%d')}"

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
