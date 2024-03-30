import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import get_parse_args


def create_plot(df, mode):
    country_names = df[['country_id', 'Country']].drop_duplicates().set_index('country_id')['Country'].to_dict()

    grouped_data = df.groupby(['year', 'country_id'])['AverageTemperatureCelsius'].mean().unstack().reset_index()

    palette = sns.color_palette("hsv", n_colors=len(df['country_id'].unique()))

    plt.figure(figsize=(12, 8))
    for i, country_id in enumerate(grouped_data.columns[1:]):
        plt.plot(grouped_data['year'], grouped_data[country_id], label=country_names.get(country_id), color=palette[i])

    plt.title('Average Temperature per Year per Each Country')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()

    if mode == "1":
        print("Saving plot to ../plots/task4c.png")
        plt.savefig('../plots/task4c.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)

