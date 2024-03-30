import matplotlib.pyplot as plt
import pandas as pd

from utils import get_parse_args


def create_plot(df, mode):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['AverageTemperatureCelsius'], facecolors='none', edgecolor='black', marker='.', alpha=0.2)
    plt.title('Average Temperature Celsius vs. Year')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Celsius (°C)')
    plt.grid(True)
    if mode == "1":
        print("Saving plot to ../plots/task2c.png")
        plt.savefig('../plots/task2c.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
