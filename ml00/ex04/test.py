import numpy as np
from prediction import predict_


x = np.arange(1, 6).reshape(-1, 1)
print("x = \n", x)
theta1 = np.array([[5], [0]])
print("with theta = 5, 0 : \n", predict_(x, theta1))
theta2 = np.array([[0], [1]])
print("with theta = 0, 1 : \n", predict_(x, theta2))
theta3 = np.array([[5], [3]])
print("with theta = 5, 3 : \n", predict_(x, theta3))
theta4 = np.array([[-3], [1]])
print("with theta = -3, 1 : \n", predict_(x, theta4))
print("Error cases :")
print(predict_(x, np.array([[0], ['a']])))
print(predict_('a', theta4))
print(predict_(x, np.array([1, 2])))
print(predict_(np.array([[1], [3], [5], ['b']]), theta4))
print(predict_(np.array([[1, 2, 3], [2, 3, 4]]), theta4))
