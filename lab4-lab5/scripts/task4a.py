import pandas as pd
import matplotlib.pyplot as plt

from utils import get_parse_args


def create_plot(df, mode):
    grouped_data = df.groupby(['year', 'country_id'])['AverageTemperatureCelsius'].mean().reset_index()

    plt.figure(figsize=(12, 8))
    plt.plot(grouped_data['year'], grouped_data['AverageTemperatureCelsius'])
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Average Temperature per Year per Each Country')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    if mode == "1":
        print("Saving plot to ../plots/task4a.png")
        plt.savefig('../plots/task4a.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
