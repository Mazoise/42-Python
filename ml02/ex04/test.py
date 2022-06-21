import numpy as np
from fit import fit_
from prediction import predict_

print("x = np.array([[0.2, 2., 20.], [0.4, 4., 40.],\
 [0.6, 6., 60.], [0.8, 8., 80.]])")
print("y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])")
print("theta = np.array([[42.], [1.], [1.], [1.]])")
x = np.array([[0.2, 2., 20.], [0.4, 4., 40.],
              [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])

theta2 = fit_(x, y, theta, alpha=0.0005, max_iter=42000)
print("Theta after fit : \n", theta2)
print("Predict :\n", predict_(x, theta2))
