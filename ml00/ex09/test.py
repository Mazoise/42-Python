import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from other_losses import mse_, rmse_, mae_, r2score_


x = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])

print("TEST 1: MSE")
print(mse_(x, y))
print(mean_squared_error(x, y))
print("TEST 2: RMSE")
print(rmse_(x, y))
print(sqrt(mean_squared_error(x, y)))
print("TEST 3: MAE")
print(mae_(x, y))
print(mean_absolute_error(x, y))
print("TEST 4: R2")
print(r2score_(x, y))
print(r2_score(x, y))
