import requests, json
from datetime import datetime, timedelta, timezone

# Your API key from OpenWeatherMap
api_key = "9268d2b7a54c466ab62450d462e8a997"

# Base URLs
base_url = "http://api.openweathermap.org/data/2.5/weather?"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"

# City input
city_name = input("Enter city name: ")

# Complete URLs
complete_url = f"{base_url}appid={api_key}&q={city_name}"
complete_forecast_url = f"{forecast_url}appid={api_key}&q={city_name}"

# API requests
response = requests.get(complete_url)
forecast_response = requests.get(complete_forecast_url)

# Parse JSON
x = response.json()
forecast_x = forecast_response.json()

# CURRENT WEATHER REPORT
if x.get("cod") == 200:
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print("\nCurrent Weather in", city_name)
    print(f"Temperature (K): {current_temperature}")
    print(f"Pressure (hPa): {current_pressure}")
    print(f"Humidity (%): {current_humidity}")
    print(f"Description: {weather_description}")
else:
    print("City Not Found or Error in Current Weather API")

# FORECAST: Will it rain in the next 3 days?
print("\nChecking forecast for rain in the next 3 days...\n")

rain_expected = False
now = datetime.now(timezone.utc)
in_three_days = now + timedelta(days=3)

for item in forecast_x.get("list", []):
    dt_txt = item["dt_txt"]
    forecast_time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

    if now <= forecast_time <= in_three_days:
        for weather in item["weather"]:
            if "rain" in weather["main"].lower():
                print(f"🌧 Rain forecasted on {dt_txt} - {weather['description']}")
                rain_expected = True
                break

if not rain_expected:
    print("No rain forecasted in the next 3 days. 🌤")
