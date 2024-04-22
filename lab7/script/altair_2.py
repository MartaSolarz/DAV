import altair as alt
import pandas as pd
import webbrowser
import sys
import os

try:
    mode = sys.argv[1]
except IndexError:
    mode = "0"

if mode not in ["0", "1"]:
    print('Invalid mode')
    sys.exit(1)

data = pd.read_csv('../data/gapminder.csv')

df = data[data['year'] == 2007][['continent', 'lifeExp']]

box_plot = alt.Chart(df).mark_boxplot().encode(
    y=alt.Y('lifeExp:Q', title='Life Expectancy'),
    x=alt.X('continent:N', title='Continent'),
    color='continent:N',
    tooltip=['year:O', 'continent:N', 'lifeExp:Q']
).properties(
    width=400,
    height=300,
    title='Life Expectancy by Continent (2007)'
)

html_file_path = '../plots/altair_2.html'
box_plot.save(html_file_path)

if mode == "0":
    webbrowser.open('file://' + os.path.realpath(html_file_path))
else:
    print('HTML file has been generated successfully. Path: plots/altair_2.html')
