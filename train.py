import csv
import sys

LEARNING_RATE = 0.1
ITERATIONS = 1000
"""
LEARNING_RATE → Tamaño del paso del gradient descent en la fórmula:
θ=θ−(alfa.gradiente) el LEARNING_RATE es alfa.
Si fuera muy grande->diverge
si fuera muy pequeño->tardaría mucho en converger
ITERATIONS → Cuántas veces repetimos el ajuste.
"""

# Load dataset
def load_data(filename):
    
    mileages = [] # lista para los km
    prices = []   # lista para precios

    try:
        with open(filename, 'r') as file: # abrimos archivo en modo lectura
            reader = csv.DictReader(file) # guardamos los datos de km y precio
            for row in reader:
                mileages.append(float(row['km'])) # pasamos el texto a float
                prices.append(float(row['price']))
    except Exception:
        print("Error loading dataset.")
        sys.exit(1)

    if len(mileages) == 0:
        print("Dataset is empty.")
        sys.exit(1)

    return mileages, prices

# Normalization
"""Normalizar es transformar los valores para que estén en una escala similar,
normalmente alrededor de 0. Esto hace que los valores estén en una escala más
pequeña y comparable"""
def normalize(data):
    """calculamos el promedio de los datos: mean,que es el valor central y la
    desviación estandar std (fórmula),que mide cómo de dispersos están los
    datos respecto a la media"""
    mean = sum(data) / len(data)
    std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    if std == 0: # pq si los valores son iguales no se puede normalizar
        return data, mean, std

    normalized = [(x - mean) / std for x in data] # fórmula de normalización
    return normalized, mean, std

def estimate_price(mileage, theta0, theta1):
    """Hypothesis: estimatePrice(mileage) = θ0 + (θ1 * mileage)"""
    return theta0 + theta1 * mileage

def train(mileages, prices):
    """Gradiente descendente. El programa se utilizará para entrenar el modelo.
    Leerá el archivo del conjunto de datos y realizará una regresión lineal
    con los datos (fórmulas dadas)."""
    theta0 = 0
    theta1 = 0
    m = len(mileages) # numero de ejemplos del dataset

    for _ in range(ITERATIONS):
        sum_error = 0
        sum_error_mileage = 0

        for i in range(m):
            prediction = estimate_price(mileages[i], theta0, theta1)
            error = prediction - prices[i] # Error = predicción - valor real

            sum_error += error  
            sum_error_mileage += error * mileages[i]

        """calculamos el promedio del gradiente"""
        tmp_theta0 = (LEARNING_RATE * sum_error) / m
        tmp_theta1 = (LEARNING_RATE * sum_error_mileage) / m

        # Actualizamos los thetas
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    return theta0, theta1

def save_parameters(theta0, theta1, mileage_mean, mileage_std):
    """Guardamos los parámetros en el archivo .csv"""
    data = {
        "theta0": theta0,
        "theta1": theta1,
        "mean": mileage_mean,
        "std": mileage_std
    }

    with open("thetas.csv", "w", newline="") as file:
         writer = csv.writer(file)
         # primera fila es la cabecera
         writer.writerow(["theta0", "theta1", "mean", "std"])
         # a partir de la 2ª fila los valores
         writer.writerow([theta0, theta1, mean, std])
          

if __name__ == "__main__":
    mileages, prices = load_data("data.csv")

    # Normalizamos x (Km)
    mileages, mean, std = normalize(mileages)
    # entrenamos el modelo
    theta0, theta1 = train(mileages, prices)

    save_parameters(theta0, theta1, mean, std)

    print("Training finished.")
    print("theta0 =", theta0)
    print("theta1 =", theta1)
