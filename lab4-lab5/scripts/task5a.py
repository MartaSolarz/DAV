import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import get_parse_args


def create_plot(df, mode):
    unique_countries = df['country_id'].unique()
    palette = sns.color_palette("hsv", n_colors=len(unique_countries))

    avg_temp_df = df.groupby(['year', 'Country'])['AverageTemperatureCelsius'].mean().reset_index()

    sns.set()
    g = sns.FacetGrid(avg_temp_df, col="Country", hue="Country", col_wrap=3, palette=palette,
                      sharex=True, sharey=True, height=2.5, aspect=1.2)
    g.map(sns.lineplot, "year", "AverageTemperatureCelsius")

    g.set_titles("{col_name}", fontsize=10)
    g.add_legend(title="Country")

    if mode == "1":
        print("Saving plot to ../plots/task5a.png")
        plt.savefig('../plots/task5a.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)