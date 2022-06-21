import numpy as np
from fit import fit_
from prediction import predict_


print("x = np.array([[12.4956442], [21.5007972], [31.5527382],\
[48.9145838], [57.5088733]])")
x = np.array([[12.4956442], [21.5007972], [31.5527382],
              [48.9145838], [57.5088733]])
print("y = np.array([[37.4013816], [36.1473236], [45.7655287],\
[46.6793434], [59.5585554]])")
y = np.array([[37.4013816], [36.1473236], [45.7655287],
              [46.6793434], [59.5585554]])
theta = np.array([[1], [1]])
theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=15000)
print("THETA after fit : \n", theta1)
print("Predict with new theta : \n", predict_(x, theta1))
