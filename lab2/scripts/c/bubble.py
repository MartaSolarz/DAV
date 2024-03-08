import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
from lab2.scripts.helper import COUNTRY_NAMES_C, AREA_C, million_formatter

DATA = '../../data/c_cleaned.csv'
OUTPUT = '../../plots/c/bubble.gif'
Y_COUNTRY_CODE = 1
Y_TEXT = 45


def update_legend(ax, scatters):
    try:
        ax.legend_.remove()
    except AttributeError:
        pass
    handles, labels = [], []
    for country, scatter in scatters.items():
        handles.append(scatter)
        labels.append(COUNTRY_NAMES_C.get(country, country))
    ax.legend(handles, labels, fontsize='large', loc='upper left')


def update(frame, years, countries, df, year_text, scatters, ax, country_texts):
    year = years[frame]
    for country in countries:
        population = df.loc[year, country]
        density = population * 1000000 / AREA_C[country]
        scatters[country].set_offsets([[year, population]])
        scatters[country].set_sizes([density])
        country_texts[country].set_position((year, df.loc[year, country]+Y_COUNTRY_CODE))
    year_text.set_text(str(year))
    update_legend(ax, scatters)


def main():
    df = pd.read_csv(DATA, index_col='Years')

    countries, years = df.columns, df.index.astype(int)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Population', fontsize=14)
    ax.set_title('Population Growth and Population Density (1960-2022)', fontsize=16)
    ax.set_xlim(1960, 2022)
    ax.set_ylim(0, df.max().max() * 1.2)
    ax.grid(True, linestyle='--', alpha=0.8)
    ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))

    year_text = ax.text(1965, Y_TEXT, '', fontsize=15)
    country_texts = {country: ax.text(1960, df[country].iloc[0]+Y_COUNTRY_CODE, country, fontsize=10, ha='center') for country in countries}

    scatters = {country: ax.scatter([], [], s=[], label=COUNTRY_NAMES_C.get(country, country)) for country in countries}

    ani = animation.FuncAnimation(fig, update, frames=len(years), fargs=(years, countries, df, year_text, scatters, ax, country_texts), interval=100, repeat=False)

    ani.save(OUTPUT, writer='imagemagick', fps=6)


if __name__ == '__main__':
    main()
