import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import get_parse_args


def create_plot(df, mode):
    unique_countries = df['Country'].unique()
    country_to_color = {country: color for country, color in
                        zip(unique_countries, sns.color_palette("hsv", len(unique_countries)))}

    palette = {row['City']: country_to_color[row['Country']] for _, row in
               df[['Country', 'City']].drop_duplicates().iterrows()}

    avg_temp_df = df.groupby(['year', 'Country', 'City'])['AverageTemperatureCelsius'].mean().reset_index()

    sns.set_style("whitegrid")
    g = sns.FacetGrid(avg_temp_df, col="Country", hue="City", col_wrap=3, palette=palette,
                      sharex=True, sharey=True, height=2.5, aspect=1.2)

    g.map(sns.lineplot, "year", "AverageTemperatureCelsius", estimator=None, lw=1, alpha=0.7)

    g.set_titles("{col_name}", fontsize=10)

    handles = [plt.Line2D([], [], color=color, marker='', linestyle='-', linewidth=2) for color in country_to_color.values()]
    labels = list(country_to_color.keys())
    g.fig.legend(handles, labels, title="Country", loc='lower right', frameon=True)

    if mode == "1":
        print("Saving plot to ../plots/task5c.png")
        plt.savefig('../plots/task5c.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
