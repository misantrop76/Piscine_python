import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load  # ta fonction de l'exo 0

gdp = load("../P2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
life = load("../P2/life_expectancy_years.csv")
gdp = gdp[['country', '1900']]
life = life[['country', '1900']]
df = pd.merge(gdp, life, on='country', suffixes=('_gdp', '_life'))
df.dropna(inplace=True)
df['1900_gdp'] = df['1900_gdp'].astype(float)
df['1900_life'] = df['1900_life'].astype(float)

# Tracer le graphique
plt.figure(figsize=(10, 7))
plt.scatter(df['1900_gdp'], df['1900_life'])
plt.xscale('log')
plt.xlabel("Gross domestic product")
plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
plt.ylabel("Life Expectancy")
plt.title("1900")
plt.show()
