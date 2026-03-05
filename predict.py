import csv
import sys

def estimate_price(mileage, theta0, theta1):
    
    return theta0 + theta1 * mileage

def load_parameters():
    try:
        with open("thetas.csv", "r") as file:
            reader = csv.DictReader(file)
            row = next(reader)

            return (
                float(row["theta0"]),
                float(row["theta1"]),
                float(row["mean"]),
                float(row["std"])
            )
        """guardamos también mean y std porque hemos entrenado el modelo con
        datos normalizados, si no normalizamos el mileage del usuario con el
        mismo mean y std, la predicción será incorrecta."""
    except Exception:
        return 0, 0, 0, 1  # default values

if __name__ == "__main__":
    theta0, theta1, mean, std = load_parameters()

    try:
        mileage = float(input("Enter mileage: "))
    except ValueError:
        print("Invalid mileage.")
        sys.exit(1)

    # Normalizamos como en el train
    if std != 0:
        mileage = (mileage - mean) / std
    # predicción
    price = estimate_price(mileage, theta0, theta1)

    print("Estimated price:", price)
