import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils import get_parse_args


def create_plot(df, mode):
    plt.figure(figsize=(12, 8))

    sns.violinplot(x='country_id', y='AverageTemperatureCelsius', data=df, color='skyblue')

    plt.title('Distribution of Temperatures Within Each Country')
    plt.xlabel('Country')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    if mode == "1":
        print("Saving plot to ../plots/task3c.png")
        plt.savefig('../plots/task3c.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
