import numpy as np
from loss import loss_

print("X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])")
X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])

print("Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])")
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])

print("loss_(X, Y)", loss_(X, Y))
print("loss_(X, X)", loss_(X, X))
