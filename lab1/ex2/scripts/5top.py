import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/5top.csv', index_col='Country Name')

df.columns = df.columns.map(lambda x: x[:4])
df = df.map(lambda x: x/1000000)

for year in df.columns:
    df.plot(kind='bar', y=year, figsize=(7, 6), legend=False)
    plt.title(f'Population growth')
    plt.xlabel('Country')
    plt.ylabel('Population size (mln)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.ylim(0, 1600)
    plt.text(0, 1500, year, fontsize=12, ha='center')
    for index, value in enumerate(df[year]):
        plt.text(index, value + 50,
                 str(int(value)),
                 ha='center',
                 fontsize=10)
    plt.savefig(f'../images/top5/{year}.jpg')