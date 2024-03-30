import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from utils import get_parse_args


def create_plot(grouped_data, data_to_plot, mode):
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
    if mode == "1":
        print("Saving plot to ../plots/task3b.png")
        plt.savefig('../plots/task3b.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")

grouped_data = df[['country_id', 'AverageTemperatureCelsius']].groupby('country_id')
data_to_plot = [group['AverageTemperatureCelsius'].values for name, group in grouped_data]

create_plot(grouped_data, data_to_plot, args.mode)
