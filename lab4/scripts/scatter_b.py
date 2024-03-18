import matplotlib.pyplot as plt
import pandas as pd


def fig2(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['AverageTemperatureCelsius'], facecolors='none', edgecolor='black', marker='.')
    plt.title('Average Temperature Celsius vs. Year')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Celsius (°C)')
    plt.grid(True)
    plt.savefig('../plots/fig2.png')


df = pd.read_csv("../data/temperatures_clean.csv")
fig2(df)
