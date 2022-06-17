import numpy as np

def loss_elem_(y, y_hat):
    """
    Description:
        Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        J_elem: numpy.array, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between y and y_hat.
        None if y or y_hat is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    if (type(y) != np.ndarray or type(y_hat) != np.ndarray
        or len(y.shape) != 2 or y.shape != y_hat.shape or y.shape[1] != 1):
        return None
    try:
        return (y_hat - y) ** 2
    except Exception:
        return None

def loss_(y, y_hat):
    """
    Description:
        Calculates the value of loss function.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        J_value : has to be a float.
        None if there is a shape matching problem between y or y_hat.
        None if y or y_hat is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    try:
        return np.sum(loss_elem_(y, y_hat)) / (2 * len(y))
    except Exception:
        return None
