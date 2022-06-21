import numpy as np
from prediction import predict_


x = np.arange(1, 13).reshape((4, 3))

print("theta1 = np.array([[5], [0], [0], [0]])")
theta1 = np.array([[5], [0], [0], [0]])
print(predict_(x, theta1))

print("theta2 = np.array([[0], [1], [0], [0]])")
theta2 = np.array([[0], [1], [0], [0]])
print(predict_(x, theta2))

print("theta3 = np.array([[-1.5], [0.6], [2.3], [1.98]]")
theta3 = np.array([[-1.5], [0.6], [2.3], [1.98]])
print(predict_(x, theta3))

print("theta4 = np.array([[-3], [1], [2], [3.5]])")
theta4 = np.array([[-3], [1], [2], [3.5]])
print(predict_(x, theta4))
