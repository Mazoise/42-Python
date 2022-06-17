import numpy as np


def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array, without any for loop.
        The two arrays must have the same dimensions.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        The half mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.array.
        None if y and y_hat does not share the same dimensions.
        None if y or y_hat is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    if (type(y) != np.ndarray or type(y_hat) != np.ndarray
       or len(y.shape) != 2 or y.shape != y_hat.shape
       or y.shape[1] != 1):
        return None
    # try:
    # tmp = np.swapaxes(y_hat - y, 0, 1)
    return (np.swapaxes(y_hat - y, 0, 1).dot(y_hat - y) / (2 * len(y)))[0][0]
    # except Exception:
    #     return None