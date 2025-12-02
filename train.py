from utils import parse_dataset, check_error_data, estimate_price

# Linear regression training with feature normalization
def train_linear_regression(dataset):
    kms = [km for km, _ in dataset]
    m = len(dataset)
    #Calculate mean (fr: moyenne) and standard deviation (fr: ecart-type)
    mean_km = sum(kms) / m
    std_km = (sum((km - mean_km) ** 2 for km in kms) / m) ** 0.5
    norm_dataset = [((km - mean_km) / std_km, price) for km, price in dataset]
    theta0 = 0.0
    theta1 = 0.0
    # Training parameters: learning rate is the number of steps during gradient descent
    # decay is the rate at which the learning rate decreases
    # iterations is the total number of iterations for training
    learning_rate = 0.05
    decay = 0.00005
    iterations = 150000
    for t in range(iterations):
        # Update learning rate with decay
        lr = learning_rate / (1 + decay * t)
        # Compute gradients
        grad0 = 0.0
        grad1 = 0.0
        for km, price in norm_dataset:
            # Predict price
            pred = theta0 + theta1 * km
            # Calculate error
            err = pred - price
            # Accumulate gradients
            grad0 += err
            grad1 += err * km
        # Update parameters
        # Divide by m to get the average gradient
        theta0 -= lr * (grad0 / m)
        theta1 -= lr * (grad1 / m)
    # Adjust theta1 and theta0 back to original scale
    theta1_final = theta1 / std_km
    theta0_final = theta0 - (theta1_final * mean_km)
    return theta0_final, theta1_final

# Main training function
def train_model():
    dataset = parse_dataset("data.csv")

    if check_error_data(dataset):
        print("Error: Dataset contains invalid data.")
        exit(1)

    theta0, theta1 = train_linear_regression(dataset)
    print(f"Model trained: theta0={theta0}, theta1={theta1}")
    return theta0, theta1

# Export model parameters to file
def save_model(theta0, theta1, file_path="model.txt"):
    with open(file_path, "w") as file:
        file.write(f"{theta0}\n{theta1}\n")

# Run training and save model
if __name__ == "__main__":
    t0, t1 = train_model()
    save_model(t0, t1)
