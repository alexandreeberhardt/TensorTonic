import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x, dtype=float)
    x = np.negative(x)
    np.exp(x)
    x = np.add(x, 1)
    np.reciprocal(x)
    return x
