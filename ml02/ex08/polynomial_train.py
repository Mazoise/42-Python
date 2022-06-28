import numpy as np
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from pandas import read_csv
import matplotlib.pyplot as plt

data = read_csv("are_blue_pills_magics.csv")
Dose = np.array(data['Micrograms']).reshape(-1, 1)
Score = np.array(data['Score']).reshape(-1, 1)
Patient = np.array(data['Patient']).reshape(-1, 1)
lr = []

thetas = [
    np.array([[90], [-9]]).reshape(-1, 1),
    np.array([[92], [-11], [0.2]]).reshape(-1, 1),
    np.array([[82], [0.2], [-3], [0.3]]).reshape(-1, 1),
    np.array([[-20], [160], [-80], [10], [-1]]).reshape(-1, 1),
    np.array([[1140], [-1850], [1110], [-305], [40], [-2]]).reshape(-1, 1),
    np.array([[9110], [-18015], [13400], [-4935],
              [966], [-96.4], [3.86]]).reshape(-1, 1),
]

alphas = [0.01, 0.001, 0.00001, 0.000001, 0.00000001, 0.000000001]

mse = np.zeros(6)

for i in range(1, 7):
    lr.append(MyLR(thetas[i - 1], alphas[i - 1], 100000))
    X_ = add_polynomial_features(Dose, i)
    lr[i - 1].fit_(X_, Score)
    mse[i - 1] = lr[i - 1].mse_(lr[i - 1].predict_(X_), Score)
    print("Model", i, " MSE : ", mse[i - 1])
plt.bar(np.arange(1, 7), mse)
plt.show()
plt.plot(Dose, Score, 'o')
for i in range(1, 7):
    continuous_dose = np.arange(np.min(Dose),
                                np.max(Dose), 0.01).reshape(-1, 1)
    continuous_dose_poly = add_polynomial_features(continuous_dose, i)
    plt.plot(continuous_dose, lr[i - 1].predict_(continuous_dose_poly),
             '-', label='Model ' + str(i))
plt.legend()
plt.xlabel("Dose")
plt.ylabel("Score")
plt.show()
