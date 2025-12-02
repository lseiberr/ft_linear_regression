from train import *
from predict import *
from visualize import *

if __name__ == "__main__":
	t0, t1 = train_model()
	mileage = get_user_mileage()
	price_estimate = estimate_price(float(mileage), t0, t1)
	print(f"Estimated price for mileage: ${price_estimate:.2f}")
	plot_regression(parse_dataset('data.csv'), t0, t1)
	print("Model evaluation metrics:")
	mse, rmse, r2 = model_precision(parse_dataset('data.csv'), t0, t1)
	print(f"MSE: {mse}, RMSE: {rmse}, R^2: {r2}")




