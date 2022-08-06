import numpy as np
import matplotlib.pyplot as plt
import math


class MyLinearRegression():
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """

    def __init__(self, theta, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta
        self.bounds = None

    def fit_(self, x, y):
        try:
            self.theta = self.theta.astype(float)
            y_norm = self.minmax_(y)
            for i in range(self.max_iter):
                try:
                    self.theta -= self.alpha * self.gradient_(x, y_norm)
                    if (math.isnan(self.theta[0])):
                        return self.theta
                except RuntimeWarning:
                    self.theta[0] = math.nan
                    return self.theta
            return self.theta
        except Exception as e:
            print("Error in fit: ", e)
            return None

    def minmax_(self, data):
        if (type(data) != np.ndarray or len(data) == 0):
            print("TypeError in minmax")
            return None
        try:
            if self.bounds is None:
                self.bounds = np.array([data.min(), data.max()])
            return (data - self.bounds[0]) / (self.bounds[1] - self.bounds[0])
        except Exception as e:
            print("Error in minmax: ", e)
            return None

    def reverse_minmax_(self, data):
        return data * (self.bounds[1] - self.bounds[0]) + self.bounds[0]

    def predict_theta_(self, x, theta):
        if (type(x) != np.ndarray or type(theta) != np.ndarray
           or len(x) == 0 or len(theta) == 0):
            print("TypeError in predict")
            return None
        try:
            x = self.add_intercept_(x)
            return x.dot(theta)
        except Exception as e:
            print("Error in predict: ", e)
            return None

    def predict_(self, x):
        return self.predict_theta_(x, self.theta)

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

    def mse_(self, y, y_hat):
        try:
            return self.loss_(y, y_hat) * 2
        except Exception as e:
            print("Error in mse: ", e)
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

    def plot_(self, x, y, xlabels=("x"), ylabel="y", units="units",
              ycolor=("navy"), predcolor=("dodgerblue")):
        for i in range(x.shape[1]):
            plt.plot(x[:, i], y, 'o',
                     label=units,
                     color=ycolor[i])
            plt.plot(x[:, i], self.reverse_minmax_(self.predict_(x)), '.',
                     color=predcolor[i],
                     label="Predicted " + units.lower())
            plt.legend()
            plt.xlabel(xlabels[i])
            plt.ylabel(ylabel)
            plt.grid()
            plt.show()
