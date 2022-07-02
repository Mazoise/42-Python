import numpy as np


def sigmoid_(x):
    """
    Compute the sigmoid of a vector.
    Args:
        x: has to be a numpy.ndarray, a vector.
    Returns:
        The sigmoid value as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if type(x) is not np.ndarray:
        print("TypeError in sigmoid")
        return None
    return np.array(1 / (1 + np.exp(-x))).reshape(-1, 1)
