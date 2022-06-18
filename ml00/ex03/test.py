import numpy as np
from tools import add_intercept


x = np.arange(1, 6).reshape((5, 1))
print("x = \n", x)
print("with interceptor: \n", add_intercept(x))
y = np.arange(1, 10).reshape((3, 3))
print("y = \n", y)
print("with interceptor: \n", add_intercept(y))
print("Error cases :")
print(add_intercept(np.array([[0], ['a']])))
print(add_intercept('a'))
print(add_intercept(np.array([1, 2])))
print(add_intercept(np.array([])))
