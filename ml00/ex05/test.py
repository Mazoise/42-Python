import numpy as np
from plot import plot


x = np.arange(1,6).reshape(-1, 1)
y = np.array([[3.74013816],[3.61473236],[4.57655287],[4.66793434],[5.95585554]])
theta1 = np.array([[4.5],[-0.2]])
plot(x, y, theta1)
theta2 = np.array([[-1.5],[2]])
plot(x, y, theta2)
theta3 = np.array([[3],[0.3]])
plot(x, y, theta3)
print("Error Cases: (Nothing should happen)")
plot(np.array([]), y, theta3)
plot(np.arange(1, 4).reshape(-1, 1), y, theta3)
plot(x, np.array(['a', 'b']), theta3)
plot(x, y, np.array([1, 2]))
plot(x, y, np.array([[1], [2], [3]]))