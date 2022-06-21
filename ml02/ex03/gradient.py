import numpy as np
from prediction import predict_
from tools import add_intercept


def gradient(x, y, theta):

    """Computes a gradient vector from three non-empty numpy.array, without any for-loop.
       The three arrays must have the compatible shapes.
    Args:
        x: has to be an numpy.array, a matrix of shape m * n.
        y: has to be an numpy.array, a vector of shape m * 1.
        theta: has to be an numpy.array, a vector (n +1) * 1.
    Return:
        The gradient as a numpy.array, a vector of shapes n * 1,
        containg the result of the formula for all j.
        None if x, y, or theta are empty numpy.array.
        None if x, y and theta do not have compatible shapes.
        None if x, y or theta is not of expected type.
    Raises:
        This function should not raise any Exception.
    """
    try:
        return (np.swapaxes(add_intercept(x), 0, 1)
                .dot(predict_(x, theta) - y) / len(x))
    except Exception as e:
        print("Error in gradient: ", e)
        return None
