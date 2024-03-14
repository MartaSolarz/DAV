import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
from lab2.scripts.helper import million_formatter

DATA = '../data/ex3_clean.csv'
OUTPUT = '../plots/ex3.gif'
Y_LIM = 70
Y_YEAR_TEXT = 63
Y_COUNTRY_CODE = 1
X = 2
SPECIAL_YEARS = [1979, 2003, 2011]
PAUSE_FRAMES = 4 * 6

names = {
    'SAU': 'Saudi Arabia',
    'AFG': 'Afghanistan',
    'IRQ': 'Iraq',
    'TKM': 'Turkmenistan',
    'SYR': 'Syria',
}

war_info = {
    1979: ('AFG', 'Soviet–Afghan War began'),
    2003: ('IRQ', 'Invasion of Iraq began'),
    2011: ('SYR', 'Syrian Civil War began'),
}

def update(year, ax, df):
    ax.clear()
    countries, population_values = df.columns, df.loc[year]
    colors = ['red' if country == war_info.get(year, (None, ))[0] else 'lightblue' for country in countries]
    ax.bar(countries, population_values, color=colors)

    ax.set_title('Population Growth (1960-2022)\nWars in the Middle East', fontsize=16)
    ax.set_xlabel('Country', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.text(0, Y_YEAR_TEXT, year, fontsize=14, ha='center')
    ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))
    ax.set_ylim(0, Y_LIM)

    full_country_names = [names.get(country, country) for country in countries]
    ax.set_xticks(range(len(full_country_names)))
    ax.set_xticklabels(full_country_names)

    for index, country in enumerate(countries):
        ax.text(index, population_values[country] + Y_COUNTRY_CODE, country, ha='center', fontsize=10)

    if year in war_info:
        event_text = war_info[year][1]
        ax.text(X, Y_YEAR_TEXT, event_text, fontsize=15, ha='center', color='red')


def main():
    df = pd.read_csv(DATA, index_col='Years')
    fig, ax = plt.subplots(figsize=(10, 6))

    frame = []
    for year in df.index:
        frame.append(year)
        if year in SPECIAL_YEARS:
            for _ in range(PAUSE_FRAMES-1):
                frame.append(year)

    anim = FuncAnimation(fig, update, fargs=(ax, df), frames=frame, repeat=False)

    anim.save(OUTPUT, dpi=200, writer='imagemagick', fps=6)


if __name__ == '__main__':
    main()
