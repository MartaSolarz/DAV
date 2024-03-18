import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fig7(df):
    plt.figure(figsize=(12, 8))

    sns.violinplot(x='country_id', y='AverageTemperatureCelsius', data=df, color='skyblue')

    plt.title('Distribution of Temperatures Within Each Country')
    plt.xlabel('Country')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('../plots/fig7.png')


df = pd.read_csv("../data/temperatures_clean.csv")
fig7(df)
