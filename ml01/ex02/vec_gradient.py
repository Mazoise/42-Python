from prediction import predict_
from tools import add_intercept
import numpy as np


def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array,
       without any for loop.
       The three arrays must have compatible shapes.
    Args:
        x: has to be a numpy.array, a matrix of shape m * 1.
        y: has to be a numpy.array, a vector of shape m * 1.
        theta: has to be a numpy.array, a 2 * 1 vector.
    Return:
        The gradient as a numpy.array, a vector of shape 2 * 1.
        None if x, y, or theta is an empty numpy.array.
        None if x, y and theta do not have compatible shapes.
        None if x, y or theta is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    return (np.swapaxes(add_intercept(x), 0, 1).dot(predict_(x, theta) - y)
            / len(x))
