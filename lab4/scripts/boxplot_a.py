import matplotlib.pyplot as plt
import pandas as pd


def fig5(grouped_data, data_to_plot):
    plt.figure(figsize=(12, 8))
    plt.boxplot(data_to_plot, labels=[name for name, group in grouped_data])
    plt.title('Distribution of Temperatures Within Each Country')
    plt.ylabel('Average Temperature (°C)')
    plt.xlabel('Country')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('../plots/fig5.png')


df = pd.read_csv("../data/temperatures_clean.csv")
grouped_data = df[['country_id', 'AverageTemperatureCelsius']].groupby('country_id')
data_to_plot = [group['AverageTemperatureCelsius'].values for name, group in grouped_data]
fig5(grouped_data, data_to_plot)
