import pandas as pd
import pygal
import sys

try:
    mode = sys.argv[1]
except IndexError:
    mode = "0"

if mode not in ["0", "1"]:
    print('Invalid mode')
    sys.exit(1)

data = pd.read_csv('../data/gapminder.csv')

df = data[data['year'] == 2007][['continent', 'lifeExp']]

def boxplot_data(group):
    sorted_lifeExp = group['lifeExp'].sort_values()
    q1 = sorted_lifeExp.quantile(0.25)
    q2 = sorted_lifeExp.quantile(0.5)
    q3 = sorted_lifeExp.quantile(0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    return {'q1': q1, 'median': q2, 'q3': q3, 'lowerfence': lower_fence, 'upperfence': upper_fence}


box_data = df.groupby('continent').apply(boxplot_data, include_groups=False).to_dict()

box_plot = pygal.Box()
box_plot.title = 'Life Expectancy by Continent (2007)'
box_plot.x_title = 'Continent'
box_plot.y_title = 'Life Expectancy'
box_plot.show_y_guides = True
box_plot.show_x_guides = True
box_plot.show_legend = True
for continent, values in box_data.items():
    box_plot.add(continent, [values['q1'], values['median'], values['q3'], values['lowerfence'], values['upperfence']])

if mode == "0":
    box_plot.render_in_browser()
else:
    box_plot.render_to_file('../plots/pygal_2.svg')
    print('SVG file has been generated successfully. Path: plots/pygal_2.svg')
