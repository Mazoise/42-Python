from matplotlib import pyplot as plt
import numpy as np
from prediction import predict_

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of shape m * 1.
        y: has to be an numpy.array, a vector of shape m * 1.
        theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exception.
    """
    print(x.shape, y.shape, theta.shape)
    if (type(x) != np.ndarray or type(y) != np.ndarray
       or type(theta) != np.ndarray or len(x) == 0
       or len(y) == 0 or len(theta) == 0
       or len(x.shape) != 2 or len(y.shape) != 2
       or len(theta.shape) != 2
       or theta.shape[1] != 1): #add check
        return None
    try:
        plt.plot(x, y, 'o')
        plt.plot(x, predict_(x, theta))
        plt.show()
    except Exception:
        return
