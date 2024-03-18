import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
from lab2.scripts.helper import million_formatter, COUNTRY_NAMES_A, HATCH_PATTERNS

DATA = '../../data/a_cleaned.csv'
OUTPUT = '../../plots/a/black&white.gif'
Y_LIM = 1600
Y_YEAR_TEXT = 1450
Y_COUNTRY_CODE = 20


def update(year, ax, df):
    ax.clear()
    countries, population_values = df.columns, df.loc[year]

    colors = plt.cm.grey(np.linspace(0.1, 0.9, len(countries)))
    ax.bar(countries, population_values, color=colors, edgecolor='black', hatch=[HATCH_PATTERNS[i % len(HATCH_PATTERNS)] for i in range(len(countries))])

    ax.set_title('Population Growth (1960-2022)', fontsize=16)
    ax.set_xlabel('Country', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.text(0, Y_YEAR_TEXT, year, fontsize=14, ha='center')
    ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))
    ax.set_ylim(0, Y_LIM)

    full_country_names = [COUNTRY_NAMES_A.get(country, country) for country in countries]
    ax.set_xticks(range(len(full_country_names)))
    ax.set_xticklabels(full_country_names)

    for index, country in enumerate(countries):
        ax.text(index, population_values[country] + Y_COUNTRY_CODE, country, ha='center', fontsize=10)


def main():
    df = pd.read_csv(DATA, index_col='Years')

    fig, ax = plt.subplots(figsize=(10, 6))

    anim = FuncAnimation(fig, update, fargs=(ax, df), frames=df.index, repeat=False)

    anim.save(OUTPUT, dpi=200, writer='imagemagick', fps=6)


if __name__ == '__main__':
    main()
