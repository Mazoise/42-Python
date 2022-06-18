import numpy as np
from gradient import simple_gradient


print("x = np.array([[12.4956442],[ 21.5007972],[ 31.5527382],\
[ 48.9145838],[ 57.5088733]])")
x = np.array([[12.4956442],[ 21.5007972],[ 31.5527382],
[ 48.9145838],[ 57.5088733]])
print("y = np.array([[37.4013816],[ 36.1473236],[ 45.7655287],\
[ 46.6793434],[ 59.5585554]])")
y = np.array([[37.4013816],[ 36.1473236],[ 45.7655287],
[ 46.6793434],[ 59.5585554]])
theta1 = np.array([[2],[ 0.7]])
print("Test : theta 2, 0.7")
print(simple_gradient(x, y, theta1))
theta2 = np.array([[1],[ -0.4]])
print("Test : theta 1, -0.4")
print(simple_gradient(x, y, theta2))
