from zscore import zscore
import numpy as np

print("X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])")
X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
print(zscore(X))
print("Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])")
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
print(zscore(Y))
