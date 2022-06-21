import numpy as np
from mylinearregression import MyLinearRegression as MyLR

print("X = np.array([[1., 1., 2., 3.],\
 [5., 8., 13., 21.],\
 [34., 55., 89., 144.]])")
print("Y = np.array([[23.], [48.], [218.]])")
print("mylr = MyLR(np.array([[1.], [1.], [1.], [1.], [1]]))")
X = np.array([[1., 1., 2., 3.],
              [5., 8., 13., 21.],
              [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLR(np.array([[1.], [1.], [1.], [1.], [1]]))

print("predict :\n", mylr.predict_(X))

print("loss elem :\n", mylr.loss_elem_(mylr.predict_(X), Y))

print("loss :\n", mylr.loss_(mylr.predict_(X), Y))

print("mylr.alpha = 1.6e-4")
print("mylr.max_iter = 200000")
print("mylr.fit(X, Y)")
mylr.alpha = 1.6e-4
mylr.max_iter = 200000
mylr.fit_(X, Y)

print("theta after fit :\n", mylr.thetas)

print("predict :\n", mylr.predict_(X))

print("loss elem :\n", mylr.loss_elem_(mylr.predict_(X), Y))

print("loss :\n", mylr.loss_(mylr.predict_(X), Y))
