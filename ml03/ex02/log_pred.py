import numpy as np
from sigmoid import sigmoid_
from interceptor import add_intercept

def logistic_predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * n.
        theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
    Raises:
        This function should not raise any Exception.
    """
    if (type(x) is not np.ndarray or type(theta) is not np.ndarray
       or len(x.shape) != 2 or len(theta.shape) != 2
       or x.shape[1] + 1 != theta.shape[0] or theta.shape[1] != 1):
        print("TypeError in logistic_predict")
        return None
    try:
        return sigmoid_(np.dot(add_intercept(x), theta))
    except Exception as e:
        print("Error in logistic_predict", e)
        return None
