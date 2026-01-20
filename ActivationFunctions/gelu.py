import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    if isinstance(x, (int, float)):
        x = np.array([x], dtype=float)
    else:
        x = np.array(x, dtype=float)
    
    erfun = np.vectorize(math.erf)
    erfpar = np.divide(x,math.sqrt(2))
    er = erfun(erfpar)
    er = np.add(er,1)
    x = np.multiply(x,er)
    x = np.divide(x,2)

    return x
