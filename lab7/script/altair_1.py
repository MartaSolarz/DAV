import altair as alt
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

slider = alt.binding_range(min=1952, max=2007, step=5)
select_year = alt.selection_point(name="select", fields=['year'],
                                  bind=slider, value={'year': 1952})

base = alt.Chart(data).mark_circle().encode(
    y=alt.Y('gdpPercap:Q', title='GDP per Capita'),
    x=alt.X('lifeExp:Q', title='Life Expectancy'),
    size=alt.Size('pop:Q', title='Population'),
    color=alt.Color('continent:N', legend=alt.Legend(title="Continent")),
    tooltip=['country:N', 'gdpPercap:Q', 'lifeExp:Q', 'pop:Q', 'continent:N']
).add_params(
    select_year
).transform_filter(
    select_year
).properties(
    width=600,
    height=400
)

html_file_path = '../plots/altair_1.html'
base.save(html_file_path)

if mode == "0":
    webbrowser.open('file://' + os.path.realpath(html_file_path))
else:
    print(f'HTML file has been generated successfully. Path: plots/altair_1.html')
