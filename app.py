import requests
import pandas as pd
from datetime import datetime

API_KEY = "5fb128bdc12e29c2c7a1cc81e0f2140c"
API_KEY = "5fb128bdc12e29c2c7a1cc81e0f2140c"
CITY = "Plovdiv"
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}"
response = requests.get(URL)
data = response.json()

def get_weather_data():
    response = requests.get(WEATHER_URL)
    data = response.json()
    weather = []

    for entry in data["list"]:
        date = datetime.fromtimestamp(entry["dt"]).date()
        temp = entry["main"]["temp"]
        rain = entry.get("rain", {}).get("3h", 0)
        humidity = entry["main"]["humidity"]
        weather.append({
            "date": date,
            "temp": temp,
            "rain": rain,
            "humidity": humidity
        })

    df = pd.DataFrame(weather)
    df = df.groupby("date").agg({
        "temp": "mean",
        "rain": "sum",
        "humidity": "mean"
    })
    return df
