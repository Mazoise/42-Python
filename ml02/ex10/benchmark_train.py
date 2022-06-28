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
train_data = split_data[0]
test_data = split_data[1]
train_y = split_data[2].reshape(-1, 1)
test_y = split_data[3].reshape(-1, 1)

lr = [[], [], []]

for x in range(3):
    train_x = train_data[:, x].reshape(-1, 1)
    test_x = test_data[:, x].reshape(-1, 1)
    for power in range(4):
        lr[x].append(MyLR(np.ones(power + 2).reshape(-1, 1), 0.01, 1000))
        poly_train_x = add_polynomial_features(train_x, power + 1)
        poly_test_x = add_polynomial_features(test_x, power + 1)
        good_alpha = False
        while good_alpha == False:
            lr[x][power].fit_(poly_train_x, train_y)
            if math.isnan(lr[x][power].theta[0]):
                lr[x][power].alpha *= 0.1
                lr[x][power].theta = np.ones(power + 2).reshape(-1, 1)
            else:
                good_alpha = True
        print(lr[x][power].theta)
        print("Model", power, " MSE : ", lr[x][power].mse_(lr[x][power].predict_(poly_test_x), test_y))

