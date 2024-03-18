import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
from lab2.scripts.helper import COUNTRY_NAMES_C, million_formatter

DATA = '../../data/c_cleaned.csv'
OUTPUT = '../../plots/c/lines.gif'
Y_TEXT = 45


def update(frame, years, countries, df, lines_data, lines, country_texts, year_text):
    year = years[frame]
    for country in countries:
        xdata, ydata = lines_data[country]
        xdata.append(year)
        ydata.append(df.loc[year, country])
        lines[country].set_data(xdata, ydata)
        country_texts[country].set_position((year, df.loc[year, country]))
    year_text.set_text(str(year))


def main():
    df = pd.read_csv(DATA, index_col='Years')
    countries, years = df.columns, df.index

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.close()

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Population', fontsize=14)
    ax.set_title('Population Growth (1960-2022)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.8)

    ax.set_xlim(1960, 2022)
    ax.set_ylim(0, df.max().max() * 1.2)
    ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))

    year_text = ax.text(1965, Y_TEXT, '', fontsize=15)

    country_texts = {country: ax.text(1960, df[country].iloc[0], country, fontsize=12, ha='center') for country in
                     countries}

    lines = {country: ax.plot([], [], label=country)[0] for country in countries}

    lines_data = {country: ([], []) for country in countries}

    ani = animation.FuncAnimation(fig, update, len(years), fargs=(years, countries, df, lines_data, lines, country_texts, year_text), interval=100, repeat=False)

    ax.legend([COUNTRY_NAMES_C.get(country, country) for country in countries], fontsize='large', loc='upper left')

    ani.save(OUTPUT, writer='imagemagick', fps=6)


if __name__ == '__main__':
    main()
