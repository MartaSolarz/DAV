import matplotlib.pyplot as plt
import pandas as pd

def fig4(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['AverageTemperatureCelsius'], facecolors='None', edgecolor='blue', marker='.', alpha=0.2)
    plt.title('Average Temperature Celsius vs. Year')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Celsius (°C)')
    plt.grid(True)
    plt.savefig('../plots/fig4.png')


df = pd.read_csv("../data/temperatures_clean.csv")
fig4(df)
