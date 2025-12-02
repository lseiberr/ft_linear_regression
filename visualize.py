import matplotlib.pyplot as plt
from utils import *

def plot_regression(dataset, theta0, theta1):
    kms = [km for km, _ in dataset]
    prices = [p for _, p in dataset]
    x_line = [min(kms), max(kms)]
    y_line = [theta0 + theta1 * x for x in x_line]
    plt.scatter(kms, prices, color='blue', label='Données réelles')
    plt.plot(x_line, y_line, color='red', label='Régression')
    plt.xlabel("Kilométrage")
    plt.ylabel("Prix")
    plt.title("Kilométrage vs Prix avec ligne de régression")
    plt.legend()
    plt.grid(True)
    plt.show()

def model_precision(dataset, theta0, theta1):
    prices = [p for _, p in dataset]
    preds = [theta0 + theta1 * km for km, _ in dataset]

    m = len(dataset)

    # MSE: Mean Squared Error is the average of the squares of the errors
    # It measures the average squared difference between predicted and actual values
    mse = sum((preds[i] - prices[i])**2 for i in range(m)) / m

    # RMSE: Root Mean Squared Error is the square root of MSE
    # It provides an error metric in the same units as the target variable
    rmse = mse**0.5

    # R^2: Coefficient of Determination
    # It indicates the proportion of variance in the dependent variable predictable from the independent variable
    mean_price = sum(prices) / m
    ss_tot = sum((p - mean_price)**2 for p in prices)
    ss_res = sum((prices[i] - preds[i])**2 for i in range(m))

    r2 = 1 - (ss_res / ss_tot)

    return mse, rmse, r2

if __name__ == "__main__":
    dataset = parse_dataset('data.csv')
    if check_error_data(dataset):
        print("Error: Dataset contains invalid data.")
        exit(1)
    theta0, theta1 = get_theta_from_file()
    plot_regression(dataset, theta0, theta1)
    mse, rmse, r2 = model_precision(dataset, theta0, theta1)
    print(f"MSE: {mse}, RMSE: {rmse}, R^2: {r2}")
