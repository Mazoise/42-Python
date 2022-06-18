import numpy as np
from prediction import simple_predict


x = np.arange(1, 6).reshape(-1, 1)
print("x = \n", x)
theta1 = np.array([[5], [0]])
print("with theta = 5, 0 : \n", simple_predict(x, theta1))
theta2 = np.array([[0], [1]])
print("with theta = 0, 1 : \n", simple_predict(x, theta2))
theta3 = np.array([[5], [3]])
print("with theta = 5, 3 : \n", simple_predict(x, theta3))
theta4 = np.array([[-3], [1]])
print("with theta = -3, 1 : \n", simple_predict(x, theta4))
print("Error cases :")
print(simple_predict(x, np.array([[0], ['a']])))
print(simple_predict('a', theta4))
print(simple_predict(x, np.array([1, 2])))
print(simple_predict(np.array([[1], [3], [5], ['b']]), theta4))
print(simple_predict(np.array([[1, 2, 3], [2, 3, 4]]), theta4))
