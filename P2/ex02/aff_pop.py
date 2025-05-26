import matplotlib.pyplot as plt
from load_csv import load


def parse_number(value):
    if isinstance(value, str):
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        else:
            return float(value)  # si pas de suffixe
    return value


def main():
    """
Display France information
    """
    df = load("../population_total.csv")
    if df is None:
        print("Erreur lors du chargement des données.")
        return
    if "France" not in df['country'].values:
        print("Aucune information pour la France")
        return
    data_fr = df[df['country'] == "France"].iloc[0]
    data_be = df[df['country'] == "Belgium"].iloc[0]

    years = df.columns[1:]
    years = [int(year) for year in years]
    values_fr = [parse_number(v) for v in data_fr[1:].astype(str)]
    values_be = [parse_number(v) for v in data_be[1:].astype(str)]
    # values_fr = values_fr[:240]
    # values_be = values_be[:240]

    plt.figure(figsize=(8, 5))
    plt.plot(years, values_be, label="Belgium", color='blue')
    plt.plot(years, values_fr, label="France", color='green')
    plt.legend()
    plt.title("Population Projections")
    plt.xlabel("years")
    plt.ylabel("Population")
    plt.xticks(ticks=range(1800, 2041, 40))
    plt.yticks(
        ticks=range(0, 80000000, 20000000),
        labels=[f"{int(y/1000000)}M" for y in range(20, 80000000, 20000000)]
    )
    plt.show()


if __name__ == "__main__":
    main()
