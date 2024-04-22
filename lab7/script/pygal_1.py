import pygal
import pandas as pd
import sys
import webbrowser
import os

try:
    mode = sys.argv[1]
except IndexError:
    mode = "0"

if mode not in ["0", "1"]:
    print('Invalid mode')
    sys.exit(1)

data = pd.read_csv('../data/gapminder.csv')

continent_colors = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'purple'
}

max_size = 50
min_size = 5
max_population = data['pop'].max()
min_population = data['pop'].min()


def normalize_size(population):
    return min_size + (population - min_population) / (max_population - min_population) * (max_size - min_size)

for year in sorted(data['year'].unique()):
    year_data = data[data['year'] == year]

    scatter_plot = pygal.XY(stroke=False, x_title='Life Expectancy', y_title='GDP per Capita',
                            title=f'Life Expectancy vs GDP per Capita ({year})',
                            tooltip_border_radius=10, dots_size=1)

    for continent, color in continent_colors.items():
        continent_data = year_data[year_data['continent'] == continent]
        scatter_plot.add(continent,
                         [{'value': (row['lifeExp'], row['gdpPercap']), 'label': row['country'],
                           'node': {'r': normalize_size(row['pop'])}}
                          for index, row in continent_data.iterrows()],
                         color=color)

    scatter_plot.render_to_file(f'../plots/pygal_1/gapminder_scatter_{year}.svg')

# for year in sorted(data['year'].unique()):
#     year_data = data[data['year'] == year]
#
#     scatter_plot = pygal.XY(stroke=False, x_title='Life Expectancy', y_title='GDP per Capita',
#                             title=f'Life Expectancy vs GDP per Capita ({year})',
#                             tooltip_border_radius=10, dots_size=1)
#
#     for continent, color in continent_colors.items():
#         continent_data = year_data[year_data['continent'] == continent]
#         scatter_plot.add(continent,
#                          [{'value': (row['lifeExp'], row['gdpPercap']), 'node': {'r': normalize_size(row['pop'])}}
#                           for index, row in continent_data.iterrows()],
#                          color=color)
#
#     scatter_plot.render_to_file(f'../plots/pygal_1/gapminder_scatter_{year}.svg')

if mode == "0":
    webbrowser.open('file://' + os.path.realpath('./plots/pygal_1/pygal_1.html'))
else:
    print('HTML file has been generated successfully. Path: plots/pygal_1/pygal_1.html')
