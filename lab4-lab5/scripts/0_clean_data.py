import requests
import pandas as pd

SOURCE = "https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/temperature.csv"

data = requests.get(SOURCE)
if data.status_code == 200:
    with open("../data/temperature.csv", "w") as file:
        file.write(data.text)

df = pd.read_csv("../data/temperature.csv")

df.dropna(subset=['City', 'Country'], inplace=True)
df.dropna(subset=['AverageTemperatureFahr', 'AverageTemperatureUncertaintyFahr'], inplace=True)

df = df[df['City'] != '']
df = df[df['Country'] != '']

df.drop(columns=['day'], inplace=True)

df['AverageTemperatureCelsius'] = (df['AverageTemperatureFahr'] - 32) / 1.8
df['AverageTemperatureUncertaintyCelsius'] = (df['AverageTemperatureUncertaintyFahr'] - 32) / 1.8

df.drop(columns=['AverageTemperatureFahr', 'AverageTemperatureUncertaintyFahr'], inplace=True)

df['City'] = df['City'].map(lambda x: "Brasilia" if x == "BrasÃ­lia" else x)

df.to_csv('../data/temperatures_clean.csv', index=False)
