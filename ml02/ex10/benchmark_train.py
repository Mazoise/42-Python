import pandas as pd
import numpy as np
import threading
import csv
from mylinearregression import MyLinearRegression as MyLR
from polynomial_model import add_polynomial_features
from data_spliter import data_spliter
import matplotlib.pyplot as plt
import math
from itertools import product


class modelThread (threading.Thread):

    def __init__(self, idx, poly_train, poly_test, mse, models, train_y, test_y):
        threading.Thread.__init__(self)
        self.idx = idx
        self.model = models[self.idx]
        self.poly_train_x = np.concatenate((poly_train[0, :, :self.model[0]],
                                    poly_train[1, :, :self.model[1]],
                                    poly_train[2, :, :self.model[2]]), axis=1)
        self.poly_test_x = np.concatenate((poly_test[0, :, :self.model[0]],
                                    poly_test[1, :, :self.model[1]],
                                    poly_test[2, :, :self.model[2]]), axis=1)
        self.train_mse = math.inf
        self.test_mse = math.inf
        self.old_train_mse = math.inf
        self.cycles = 0
        lr.append(MyLR(np.ones(self.poly_train_x.shape[1] + 1).reshape(-1, 1), 1, 100))
    # print(poly_train_x.shape)
    def run(self):
        print("Model", self.idx, self.model)
        while self.cycles < 100 or self.old_train_mse - self.train_mse > self.train_mse * 0.000001:
            self.old_train_mse = self.train_mse
            lr[self.idx].fit_(self.poly_train_x, train_y)
            if math.isnan(lr[self.idx].theta[0]):
                print("Model", self.idx, "Alpha :", lr[self.idx].alpha)
                lr[self.idx].alpha *= 0.1
                lr[self.idx].theta = np.ones(self.poly_train_x.shape[1] + 1).reshape(-1, 1)
                self.train_mse = math.inf
            else:
                self.train_mse = lr[self.idx].mse_(lr[self.idx].reverse_minmax_(lr[self.idx].predict_(self.poly_train_x)), train_y)
            self.cycles += 1
            print("Model", self.idx, "MSE :", self.train_mse)
        # print(lr[self.idx].theta)
        mse[self.idx] = lr[self.idx].mse_(lr[self.idx].reverse_minmax_(lr[self.idx].predict_(self.poly_test_x)), test_y)
        print("Model", self.idx + 1, "test MSE :", mse[self.idx], ", train MSE : ", self.train_mse)


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

threads = []
thread_list = []

for idx in range(len(models)):
    threads.append(modelThread(idx, poly_train, poly_test, mse, models, train_y, test_y))
for idx in range(len(models)):
    threads[idx].start()
    thread_list.append(threads[idx])
for t in thread_list:
    t.join()
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
    plt.plot(test_x, lr[idx].reverse_minmax_(lr[idx].predict_(poly_test_x)),
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
