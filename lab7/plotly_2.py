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

data = pd.read_csv('./data/gapminder.csv')

df = data[data['year'] == 2007][['continent', 'lifeExp']]

fig = px.box(df, x="continent", y="lifeExp", color="continent", labels={"lifeExp": "Life Expectancy", 'continent': 'Continent'}, title="Life Expectancy by Continent (2007)")

fig.update_yaxes(range=[0, 100])

if mode == "0":
    fig.show()
else:
    fig.write_html('./plots/plotly_2.html')
    print('HTML file has been generated successfully. Path: plots/plotly_2.html')
