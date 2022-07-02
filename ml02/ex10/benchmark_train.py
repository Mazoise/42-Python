import pandas as pd
import numpy as np
import csv
from mylinearregression import MyLinearRegression as MyLR
from polynomial_model import add_polynomial_features
from data_spliter import data_spliter
import matplotlib.pyplot as plt
import math
from itertools import product

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

poly_train = np.array([add_polynomial_features(train_data[:, x].reshape(-1, 1), 4)
              for x in range(3)])
poly_test = np.array([add_polynomial_features(test_data[:, x].reshape(-1, 1), 4)
             for x in range(3)])
lr = []
models = list(product([1, 2, 3, 4], repeat=3))
mse = np.ones(len(models))

for idx in range(len(models)):
    poly_train_x = np.concatenate((poly_train[0, :, :models[idx][0]],
                                   poly_train[1, :, :models[idx][1]],
                                   poly_train[2, :, :models[idx][2]]), axis=1)
    poly_test_x = np.concatenate((poly_test[0, :, :models[idx][0]],
                                   poly_test[1, :, :models[idx][1]],
                                   poly_test[2, :, :models[idx][2]]), axis=1)
    # print(poly_train_x.shape)
    print(models[idx])
    lr.append(MyLR(np.ones(poly_train_x.shape[1] + 1).reshape(-1, 1), 1, 10000))
    good_alpha = False
    while good_alpha == False:
        lr[idx].fit_(poly_train_x, train_y)
        if math.isnan(lr[idx].theta[0]):
            lr[idx].alpha *= 0.1
            lr[idx].theta = np.ones(poly_train_x.shape[1] + 1).reshape(-1, 1)
        else:
            good_alpha = True
    # print(lr[idx].theta)
    mse[idx] = lr[idx].mse_(lr[idx].predict_(poly_test_x), test_y)
    print("Model", idx + 1, " MSE : ", mse[idx], ", train MSE : ", lr[idx].mse_(lr[idx].predict_(poly_train_x), train_y))
idx = np.argmin(mse)
print(idx)
model_data = pd.DataFrame(columns=['model', 'mse', 'thetas'])
for i in range(len(models)):
    model_data.loc[i] = [' '.join(map(str, models[i])), mse[i], ' '.join(map(str, lr[i].theta.squeeze()))]
model_data.to_csv("models.csv")
for var in range(3):
    test_x = test_data[:, var]
    train_x = train_data[:, var]
    poly_test_x = np.concatenate((poly_test[0, :, :models[idx][0]],
                                   poly_test[1, :, :models[idx][1]],
                                   poly_test[2, :, :models[idx][2]]), axis=1)
    plt.plot(train_x, train_y, 'or', label='Train data')
    plt.plot(test_x, test_y, 'og', label='Test data')
    plt.plot(test_x, lr[idx].predict_(poly_test_x),
            '.', label='Model ' + str(idx + 1))
    plt.ylim([min(np.min(train_y), np.min(test_y)) - 100,
            max(np.max(train_y), np.max(test_y)) + 100])
    plt.xlim([min(np.min(train_x), np.min(test_x)) - 10,
            max(np.max(train_x), np.max(test_x)) + 10])
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

plt.bar(list(map(str, models)), mse)
plt.xticks(rotation=90)
plt.show()
