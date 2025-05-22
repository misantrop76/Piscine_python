import matplotlib.pyplot as plt
from load_csv import load

def main():
    """
Display France information
    """
    df = load("../life_expectancy_years.csv")
    if df is None:
        print("Erreur lors du chargement des données.")
        return
    if "France" not in df['country'].values:
        print(f"Aucune information pour la France")
        return
    data = df[df['country'] == "France"].iloc[0]

    years = df.columns[1:]
    values = data[1:].astype(float)

    plt.figure(figsize=(8, 5))
    plt.plot(years, values, label="France", color='blue')
    plt.title("France Life Expectancy Projections")
    plt.xlabel("years")
    plt.ylabel("Life Expectancy (Years)")
    plt.xticks(ticks=years[::40])
    plt.show()

if __name__ == "__main__":
    main()
