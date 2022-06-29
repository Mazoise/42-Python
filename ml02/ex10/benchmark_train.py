import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
from polynomial_model import add_polynomial_features
from data_spliter import data_spliter
import matplotlib.pyplot as plt
import math

data = pd.read_csv("space_avocado.csv")
weight = np.array(data['weight']).reshape(-1, 1)
prod_distance = np.array(data['prod_distance']).reshape(-1, 1)
time_delivery = np.array(data['time_delivery']).reshape(-1, 1)
target = np.array(data['target']).reshape(-1, 1)

split_data = data_spliter(np.concatenate((weight,
                                          prod_distance,
                                          time_delivery),
                                         axis=1), target, 0.6)
train_data = split_data[0].reshape(-1, 1)
test_data = split_data[1].reshape(-1, 1)
train_y = split_data[2].reshape(-1, 1)
test_y = split_data[3].reshape(-1, 1)

poly_train = [add_polynomial_features(train_data[:, x], 4)
              for x in range(3)]
poly_test = [add_polynomial_features(test_data[:, x], 4)
             for x in range(3)]
lr = []
mse = []

train_x = train_data
test_x = test_data
for power in range(4):
    lr.append(MyLR(np.ones(power + 2).reshape(-1, 1), 1, 1000000))
    poly_train_x = add_polynomial_features(train_x, power + 1)
    poly_test_x = add_polynomial_features(test_x, power + 1)
    good_alpha = False
    while good_alpha == False:
        lr[power].fit_(poly_train_x, train_y)
        if math.isnan(lr[power].theta[0]):
            lr[power].alpha *= 0.1
            lr[power].theta = np.ones(power + 2).reshape(-1, 1)
        else:
            good_alpha = True
    print(lr[power].theta)
    mse.append(lr[power].mse_(lr[power].predict_(poly_test_x), test_y))
    print("Model", power + 1, " MSE : ", mse[power])
    continuous_x = np.arange(np.min(test_x),
                                np.max(test_x), 0.01).reshape(-1, 1)
    continuous_x_poly = add_polynomial_features(continuous_x, power + 1)
    plt.plot(continuous_x, lr[power].predict_(continuous_x_poly),
            '-', label='Model ' + str(power + 1))
plt.plot(train_x, train_y, 'or', label='Train data')
plt.plot(test_x, test_y, 'og', label='Test data')
plt.ylim([min(np.min(train_y), np.min(test_y)) - 100,
          max(np.max(train_y), np.max(test_y)) + 100])
plt.xlim([min(np.min(train_x), np.min(test_x)) - 100,
          max(np.max(train_x), np.max(test_x)) + 100])
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.bar(np.arange(1, 5), mse)
plt.show()
