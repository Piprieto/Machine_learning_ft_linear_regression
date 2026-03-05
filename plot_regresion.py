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


def load_parameters():
    with open("thetas.csv", "r") as file:
        reader = csv.DictReader(file)
        row = next(reader)

        return (
            float(row["theta0"]),
            float(row["theta1"]),
            float(row["mean"]),
            float(row["std"])
        )


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


if __name__ == "__main__":
    mileages, prices = load_data("data.csv")
    theta0, theta1, mean, std = load_parameters()

    # Normalizamos los km
    normalized = [(x - mean) / std for x in mileages]

    # Calculamos predicciones
    predictions = [
        estimate_price(x, theta0, theta1)
        for x in normalized
    ]

    # Dibujamos datos reales
    plt.scatter(mileages, prices, label="Real data")

    # Dibujamos recta de la regresión
    plt.plot(mileages, predictions, color="red", label="Regression line")

    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.legend()
    plt.title("Linear Regression Result")

    plt.show()
