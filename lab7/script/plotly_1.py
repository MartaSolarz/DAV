import plotly.express as px
import sys
import pandas as pd

try:
    mode = sys.argv[1]
except IndexError:
    mode = "0"

if mode not in ["0", "1"]:
    print('Invalid mode')
    sys.exit(1)

df = pd.read_csv('../data/gapminder.csv')

fig = px.scatter(df, x="lifeExp", y="gdpPercap", animation_frame="year", size="pop", color="continent",
                 hover_name="country", size_max=60, range_y=[-10000, 50000], range_x=[0, df.lifeExp.max()+10], labels={"pop": "Population", "lifeExp": "Life Expectancy", "gdpPercap": "GDP per Capita", 'year': 'Year', 'continent': 'Continent', 'country': 'Country'}, title="Global Development Metrics Over Time")

fig.add_annotation(
    xref="paper", yref="paper",
    x=1, y=0,
    text="Circle Size represents population of the country",
    showarrow=False,
    align="right"
)

if mode == "0":
    fig.show()
else:
    fig.write_html('../plots/plotly_1.html')
    print('HTML file has been generated successfully. Path: plots/plotly_1.html')
