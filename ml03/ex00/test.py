from sigmoid import sigmoid_
import numpy as np


x = np.array(-4)
print(sigmoid_(x))

x = np.array(2)
print(sigmoid_(x))

x = np.array([[-4], [2], [0]])
print(sigmoid_(x))
