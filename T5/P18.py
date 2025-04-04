import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")
print("First 10 rows of weather data:")
print(df.head(10))
print("\nMaximum temperature:", df["temperature"].max())
print("Minimum temperature:", df["temperature"].min())
print("\nPlaces with temperature < 28°C:")
print(df[df["temperature"] < 28][["place", "temperature"]])
print("\nPlaces with Cloudy weather:")
print(df[df["weather"] == "Cloudy"][["place", "weather"]])
print("\nWeather type frequency:")
print(df["weather"].value_counts().sort_index())

plt.figure(figsize=(10, 5))
plt.bar(df["date"], df["temperature"], color='orange')
plt.title("Daily Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
