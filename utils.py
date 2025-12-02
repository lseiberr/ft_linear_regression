import os
# Estimate price based on mileage and model parameters
def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

#Parse dataset from CSV file
def parse_dataset(file_path):
    if not file_path.endswith('.csv'):
        return []
    if not os.path.isfile(file_path):
        return []
    dataset = []
    with open(file_path, 'r') as file:
        header = file.readline().strip()
        if header != "km,price":
            return []
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 2:
                return []
            km, price = map(float, parts)
            dataset.append((km, price))
    return dataset

# Check for errors in dataset
def check_error_data(dataset):
    if not dataset:
        return True
    for km, price in dataset:
        if not isinstance(km, float) or not isinstance(price, float):
            return True
    return False

# Get model parameters from file
def get_theta_from_file(file_path='model.txt'):
    if not file_path.endswith('.txt'):
        return None
    if not os.path.isfile(file_path):
        return None
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) != 2:
                raise ValueError("Model file is corrupted.")
            theta0 = float(lines[0].strip())
            theta1 = float(lines[1].strip())
            return theta0, theta1
    except Exception as e:
        print(f"Error reading model parameters: {e}")
