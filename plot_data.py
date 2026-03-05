import csv
import matplotlib.pyplot as plt

def load_data(filename):
    mileages = []
    prices = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mileages.append(float(row['km']))
            prices.append(float(row['price']))

    return mileages, prices


if __name__ == "__main__":
    mileages, prices = load_data("data.csv")

    # Gráfico de puntos (scatter)
    plt.scatter(mileages, prices)

    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.title("Car Price Dataset")

    plt.show()
