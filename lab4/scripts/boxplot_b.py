import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def fig6(grouped_data, data_to_plot):
    plt.figure(figsize=(12, 8))
    plt.boxplot(data_to_plot, labels=[name for name, group in grouped_data])
    for i, (name, group) in enumerate(grouped_data, start=1):
        jitter = np.random.normal(0, 0.09, size=len(group))
        plt.plot(np.array([i]) + jitter, group['AverageTemperatureCelsius'], alpha=0.2, color='blue', marker='.', linestyle='None')

    plt.title('Distribution of Temperatures Within Each Country')
    plt.ylabel('Average Temperature (°C)')
    plt.xlabel('Country')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('../plots/fig6.png')


df = pd.read_csv("../data/temperatures_clean.csv")
grouped_data = df[['country_id', 'AverageTemperatureCelsius']].groupby('country_id')
data_to_plot = [group['AverageTemperatureCelsius'].values for name, group in grouped_data]
fig6(grouped_data, data_to_plot)
