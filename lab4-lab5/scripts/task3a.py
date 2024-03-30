import matplotlib.pyplot as plt
import pandas as pd

from utils import get_parse_args


def create_plot(grouped_data, data_to_plot, mode):
    plt.figure(figsize=(12, 8))
    plt.boxplot(data_to_plot, labels=[name for name, group in grouped_data])
    plt.title('Distribution of Temperatures Within Each Country')
    plt.ylabel('Average Temperature (°C)')
    plt.xlabel('Country')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    if mode == "1":
        print("Saving plot to ../plots/task3a.png")
        plt.savefig('../plots/task3a.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")

grouped_data = df[['country_id', 'AverageTemperatureCelsius']].groupby('country_id')
data_to_plot = [group['AverageTemperatureCelsius'].values for name, group in grouped_data]

create_plot(grouped_data, data_to_plot, args.mode)
