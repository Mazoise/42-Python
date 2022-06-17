import numpy as np
from tools import add_intercept

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of shape m * 1.
        theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
        y_hat as a numpy.array, a vector of shape m * 1.
        None if x or theta are empty numpy.array.
        None if x or theta shapes are not appropriate.
        None if x or theta is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    if (type(x) != np.ndarray or type(theta) != np.ndarray
       or len(x) == 0 or len(theta) == 0
       or len(x.shape) != 2 or len(theta.shape) != 2
       or theta.shape[1] != 1
       or theta.shape[0] != x.shape[1] + 1):
        return None
    try:
        x = add_intercept(x)
        return x.dot(theta)
    except Exception:
        return None
