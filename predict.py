from utils import estimate_price, get_theta_from_file

theta0 = 0.0
theta1 = 0.0

# Get user input for mileage
def get_user_mileage():
	mileage = input("Enter your car's mileage: ")
	while not mileage.isdigit():
		print("Please enter a valid number for mileage.")
		mileage = input("Enter your car's mileage: ")
	return mileage

# Main execution
if __name__ == "__main__":
	mileage = get_user_mileage()
	if get_theta_from_file() is not None:
		theta0, theta1 = get_theta_from_file()
	price = estimate_price(float(mileage), theta0, theta1)
	print(f"Estimated price of the car: ${price:.2f}")
