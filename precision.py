import csv

"""Medición de la precisión del modeo. Hay varias formas:
MSE: error cuadrático medio
RMSE: Root Mean Square Error
R2: coeficiente de determinación"""

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

    # Normalizamos
    normalized_mileages = [(x - mean) / std for x in mileages]

    predictions = [
        estimate_price(x, theta0, theta1)
        for x in normalized_mileages
    ]

    # MSE
    mse = sum((predictions[i] - prices[i]) ** 2 for i in range(len(prices))) / len(prices)

    # RMSE
    rmse = mse ** 0.5

    # R2
    mean_price = sum(prices) / len(prices)
    ss_total = sum((p - mean_price) ** 2 for p in prices)
    ss_res = sum((prices[i] - predictions[i]) ** 2 for i in range(len(prices)))

    r2 = 1 - (ss_res / ss_total)

    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R2:", r2)
