import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import get_parse_args


def create_plot(df, mode):
    unique_cities = df['City'].unique()
    city_to_color = {city: color for city, color in
                        zip(unique_cities, sns.color_palette("hsv", len(unique_cities)))}

    palette = {row['City']: city_to_color[row['City']] for _, row in
               df[['Country', 'City']].drop_duplicates().iterrows()}

    avg_temp_df = df.groupby(['year', 'Country', 'City'])['AverageTemperatureCelsius'].mean().reset_index()

    sns.set_style("whitegrid")
    g = sns.FacetGrid(avg_temp_df, col="Country", hue="City", col_wrap=3, palette=palette,
                      sharex=True, sharey=True, height=2.5, aspect=1.2)

    g.map(sns.lineplot, "year", "AverageTemperatureCelsius", estimator=None, lw=1, alpha=0.7)

    g.set_titles("{col_name}", fontsize=10)
    g.add_legend(title="City")
    plt.subplots_adjust(top=0.9)

    if mode == "1":
        print("Saving plot to ../plots/task5d.png")
        plt.savefig('../plots/task5d.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
