import numpy as np
from log_pred import logistic_predict_


x = np.array([4]).reshape((-1, 1))
theta = np.array([[2], [0.5]])
print("\n", logistic_predict_(x, theta))

x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
print("\n", logistic_predict_(x2, theta2))

x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
print("\n", logistic_predict_(x3, theta3))
