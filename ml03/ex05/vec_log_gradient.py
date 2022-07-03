import numpy as np
from log_pred import logistic_predict_
from interceptor import add_intercept


def vec_log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray,
       without any for-loop. The three arrays must have comp
    Args:
        x: has to be an numpy.ndarray, a matrix of shape m * n.
        y: has to be an numpy.ndarray, a vector of shape m * 1.
        theta: has to be an numpy.ndarray, a vector (n +1) * 1.
    Returns:
        The gradient as a numpy.ndarray, a vector of shape n * 1,
        containg the result of the formula for all j.
        None if x, y, or theta are empty numpy.ndarray.
        None if x, y and theta do not have compatible shapes.
    Raises:
        This function should not raise any Exception.
    """
    if (type(x) is not np.ndarray or type(y) is not np.ndarray
       or type(theta) is not np.ndarray or x.size == 0 or y.size == 0
       or theta.size == 0 or x.shape[1] + 1 != theta.shape[0]
       or x.shape[0] != y.shape[0] or y.shape[1] != 1 or theta.shape[1] != 1):
        print("TypeError in log_gradient")
        return None
    try:
        return np.dot(add_intercept(x).T, logistic_predict_(x, theta) - y) / x.shape[0]
    except Exception as e:
        print("Error in log_gradient", e)
        return None
