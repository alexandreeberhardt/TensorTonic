import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.asarray(x, dtype=float)
    e1 = np.exp(x)
    e2 = np.exp(-x)
    num = np.subtract(e1,e2)
    den = np.add(e1,e2)
    x = np.divide(num,den)
    return x
