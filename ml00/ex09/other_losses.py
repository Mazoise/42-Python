import numpy as np
import math

def mse_(y, y_hat):
    """
    Description:
        Calculate the MSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of shape m * 1.
        y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching shape problem.
    Raises:
        This function should not raise any Exception.
    """
    if (type(y) != np.ndarray or type(y_hat) != np.ndarray
       or len(y.shape) != 2 or y.shape != y_hat.shape
       or y.shape[1] != 1):
        return None
    try:
        return (np.swapaxes(y_hat - y, 0, 1).dot(y_hat - y) / len(y))[0][0]
    except Exception:
        return None

def rmse_(y, y_hat):
    """
    Description:
        Calculate the RMSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of shape m * 1.
        y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
        rmse: has to be a float.
        None if there is a matching shape problem.
    Raises:
        This function should not raise any Exception.
    """
    try:
        return math.sqrt(mse_(y, y_hat))
    except Exception:
        return None

def mae_(y, y_hat):
    """
    Description:
        Calculate the MAE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of shape m * 1.
        y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
        mae: has to be a float.
        None if there is a matching shape problem.
    Raises:
        This function should not raise any Exception.
    """
    if (type(y) != np.ndarray or type(y_hat) != np.ndarray
       or len(y.shape) != 2 or y.shape != y_hat.shape
       or y.shape[1] != 1):
        return None
    try:
        return np.sum(abs(y_hat - y) / len(y))
    except Exception as e:
        return None

def r2score_(y, y_hat):
    """
    Description:
        Calculate the R2score between the predicted output and the output.
    Args:
        y: has to be a numpy.array, a vector of shape m * 1.
        y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
        r2score: has to be a float.
        None if there is a matching shape problem.
    Raises:
        This function should not raise any Exception.
    """
    try:
        return 1 - (np.swapaxes(y_hat - y, 0, 1).dot(y_hat - y) / (np.swapaxes(y - y.mean(0), 0, 1).dot(y - y.mean(0))))[0][0]
    except Exception:
        return None