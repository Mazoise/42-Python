import numpy as np
import matplotlib.pyplot as plt
import math


class MyLinearRegression():
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def fit_(self, x, y):
        try:
            self.thetas = self.thetas.astype(float)
            for i in range(self.max_iter):
                self.thetas -= self.alpha * self.gradient_(x, y)
            return self.thetas
        except Exception as e:
            print("Error in fit: ", e)
            return None

    def predict_thetas_(self, x, thetas):
        if (type(x) != np.ndarray or type(thetas) != np.ndarray
           or len(x) == 0 or len(thetas) == 0):
            print("TypeError in predict")
            return None
        try:
            x = self.add_intercept_(x)
            return x.dot(thetas)
        except Exception as e:
            print("Error in predict: ", e)
            return None

    def predict_(self, x):
        return self.predict_thetas_(x, self.thetas)

    @staticmethod
    def loss_elem_(y, y_hat):
        if (type(y) != np.ndarray or type(y_hat) != np.ndarray
           or len(y) == 0 or len(y_hat) == 0):
            print("TypeError in loss_elem")
            return None
        try:
            return (y_hat - y) ** 2
        except Exception as e:
            print("Error in loss_elem: ", e)
            return None

    @staticmethod
    def loss_(y, y_hat):
        if (type(y) != np.ndarray or type(y_hat) != np.ndarray
           or len(y) == 0 or len(y_hat) == 0):
            print("TypeError in loss")
            return None
        try:
            return (np.swapaxes(y_hat - y, 0, 1).dot(y_hat - y)
                    / (2 * len(y)))[0][0]
        except Exception as e:
            print("Error in loss: ", e)
            return None

    def gradient_(self, x, y):
        try:
            return (np.swapaxes(self.add_intercept_(x), 0, 1)
                    .dot(self.predict_(x) - y) / len(x))
        except Exception as e:
            print("Error in gradient: ", e)
            return None

    @staticmethod
    def add_intercept_(x):
        if (type(x) != np.ndarray or len(x) == 0):
            print("TypeError in add intercept")
            return None
        try:
            return np.insert(x, 0, 1, axis=1).astype(float)
        except Exception as e:
            print("Error in add_interceptor: ", e)
            return None
