import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "a622eba2e27081ff07ebe9c036e53d79"
city = "Mumbai"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

dates = []
temps = []

for entry in data["list"]:
    dates.append(entry["dt_txt"])
    temps.append(entry["main"]["temp"])

df = pd.DataFrame({"Date-Time": dates, "Temperature (°C)": temps})

plt.figure(figsize=(10,5))
plt.plot(df["Date-Time"], df["Temperature (°C)"])
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast for {city}")
plt.show()
