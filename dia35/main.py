import  requests
from twilio.rest import Client

api_key="REMOVIDO"
end_point = "https://api.themoviedb.org/3/search/movie?api_key="
account_sid = "<KEY>"
auth_token = "<PASSWORD>"

weather_params = {
    "lat":4222,
    "lon":-1587,
    "appid":api_key,
    "count":4
}
response=requests.get(end_point,params=weather_params)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False

for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    client=Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain!",
        from_=+57320959411,
        to=+57320959411
    )

