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

    sns.set_theme(style="whitegrid")
    g = sns.FacetGrid(avg_temp_df, col="Country", hue="City", col_wrap=3, palette=palette,
                      sharex=True, sharey=True, height=2.5, aspect=1.2)

    g.map(sns.lineplot, "year", "AverageTemperatureCelsius", estimator=None, lw=1, alpha=0.7)

    g.set_titles("{col_name}", fontsize=10, font='Times New Roman')
    g.set_axis_labels("", "")
    g.fig.suptitle('Average Temperature', fontsize=18, font='Times New Roman')
    g.fig.text(0.5, 0.01, 'Year Of Observation', ha='center', va='center', font='Times New Roman')
    g.fig.text(0.02, 0.5, 'Average Temperature (°C)', ha='center', va='center', rotation='vertical', font='Times New Roman')
    g.add_legend(title="City")
    plt.yticks(ticks=range(-5, 26, 5))
    plt.xticks(ticks=range(1750, 2020, 50))

    for ax in g.axes.flat:
        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_horizontalalignment('right')
            label.set_fontsize(10)
            label.set_fontname('Times New Roman')

    plt.subplots_adjust(top=0.9)

    if mode == "1":
        print("Saving plot to ../plots/task5e.png")
        plt.savefig('../plots/task5e.png')
    else:
        plt.show()


args = get_parse_args()
df = pd.read_csv("../data/temperatures_clean.csv")
create_plot(df, args.mode)
