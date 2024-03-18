import matplotlib.pyplot as plt
import pandas as pd


def fig1(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['AverageTemperatureCelsius'], facecolors='none', edgecolor='black')
    plt.title('Average Temperature Celsius vs. Year')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Celsius (°C)')
    plt.savefig('../plots/fig1.png')


df = pd.read_csv("../data/temperatures_clean.csv")
fig1(df)
