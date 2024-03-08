import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
from lab2.scripts.helper import COUNTRY_NAMES_A, million_formatter

DATA = '../../data/a_cleaned.csv'
OUTPUT = '../../plots/a/other.gif'
Y_COUNTRY_CODE = 20
Y_TEXT = 2700
Y_MAX = 4500


def update(frame, years, ax, df, stack_collections, year_text, country_texts):
    year = years[frame]
    data_up_to_year = df.loc[:year]

    cumulative_data = data_up_to_year.cumsum(axis=1)
    for collection in stack_collections:
        collection.remove()
    stack_collections.clear()

    colors = plt.cm.pink(np.linspace(0.1, 0.8, len(df.columns)))
    stack_collections.extend(ax.stackplot(data_up_to_year.index, data_up_to_year.T, colors=colors))
    for country in df.columns:
        if df.columns.get_loc(country) == 0:
            top_edge = df.loc[year, country]
        else:
            top_edge = cumulative_data.loc[year, country]
        country_texts[country].set_position((year, top_edge + Y_COUNTRY_CODE))
    year_text.set_text(str(year))
    ax.legend([COUNTRY_NAMES_A.get(country, country) for country in df.columns], fontsize='large', loc='upper left')


def main():
    df = pd.read_csv(DATA, index_col='Years')
    years = df.index.astype(int)
    countries = df.columns

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Population', fontsize=14)
    ax.set_title('Population Growth (1960-2022)', fontsize=16)
    ax.set_xlim(df.index.min(), df.index.max())
    ax.set_ylim(0, Y_MAX)
    ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))

    stack_collections = []
    year_text = ax.text(1965, Y_TEXT, '', fontsize=15)
    country_texts = {country: ax.text(1960, df[country].iloc[0] + Y_COUNTRY_CODE, country, fontsize=10, ha='center') for country in countries}

    ani = animation.FuncAnimation(fig, update, frames=len(years), fargs=(years, ax, df, stack_collections, year_text, country_texts), interval=100, repeat=False)

    ani.save(OUTPUT, writer='imagemagick', fps=6)


if __name__ == '__main__':
    main()
