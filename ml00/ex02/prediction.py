import numpy as np


def simple_predict(x, theta):
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
       or x.shape[1] != 1 or theta.shape[1] != 1
       or theta.shape[0] != 2):
        return None
    try:
        return x * float(theta[1]) + theta[0]
    except Exception:
        return None
