import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([[1], [0], [1]])
mylr = MyLR([2, 0.5, 7.1, -4.3, 2.09])

print("predict: \n", mylr.predict_(X))
print("loss: \n", mylr.loss_(mylr.predict_(X),Y))
mylr.fit_(X, Y)
print("theta: \n", mylr.theta)
print("predict: \n", mylr.predict_(X))
print("loss: \n", mylr.loss_(mylr.predict_(X),Y))
