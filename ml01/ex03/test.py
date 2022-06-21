import numpy as np
from my_linear_regression import MyLinearRegression as MyLR

print("x = np.array([[12.4956442], [21.5007972],\
[31.5527382], [48.9145838], [57.5088733]])")
print("y = np.array([[37.4013816], [36.1473236],\
[45.7655287], [46.6793434], [59.5585554]])")
x = np.array([[12.4956442], [21.5007972],
              [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236],
              [45.7655287], [46.6793434], [59.5585554]])
print("lr1 = MyLR(np.array([[2], [0.7]]))")
lr1 = MyLR(np.array([[2], [0.7]]))

print("lr1.predict_(x)")
print(lr1.predict_(x))
print("lr1.loss_elem_(lr1.predict_(x), y)")
print(lr1.loss_elem_(lr1.predict_(x), y))

print("lr1.loss_(lr1.predict_(x), y)")
print(lr1.loss_(lr1.predict_(x), y))

print("lr2 = MyLR(np.array([[1], [1]]), 5e-8, 1500000)")
lr2 = MyLR(np.array([[1], [1]]), 5e-8, 1500000)

print("lr2.fit_(x, y)")

print("lr2.thetas")
print(lr2.thetas)

print("lr2.predict_(x)")
print(lr2.predict_(x))

print("lr2.loss_elem_(lr2.predict_(x), y)")
print(MyLR.loss_elem_(lr2.predict_(x), y))

print("lr2.loss_(lr2.predict_(x), y)")
print(MyLR.loss_(lr2.predict_(x), y))
