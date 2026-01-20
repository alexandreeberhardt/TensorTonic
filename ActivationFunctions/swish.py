import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x, dtype=float)
    x = np.negative(x)
    x = np.exp(x)
    x = np.add(x, 1)
    x = np.reciprocal(x)
    return x

def swish(x):
    """
    Implement Swish activation function.
    """
    if isinstance(x, (int, float)):
        x = np.array([x], dtype=float)
    else:
        x = np.array(x, dtype=float)
    return np.multiply(x,sigmoid(x))
