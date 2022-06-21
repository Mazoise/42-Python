import numpy as np
from tools import add_intercept


def predict_(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of shapes m * n.
        theta: has to be an numpy.array, a vector of shapes (n + 1) * 1.
    Return:
        y_hat as a numpy.array, a vector of shapes m * 1.
        None if x or theta are empty numpy.array.
        None if x or theta shapes are not appropriate.
        None if x or theta is not of expected type.
    Raises:
        This function should not raise any Exception.
    """

    if (type(x) != np.ndarray or type(theta) != np.ndarray
       or len(x) == 0 or len(theta) == 0):
        return None
    try:
        x = add_intercept(x)
        return x.dot(theta)
    except Exception:
        return None
