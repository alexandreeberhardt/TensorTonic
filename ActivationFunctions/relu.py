import numpy as np

def relu(x):
    x = np.asarray(x, dtype=float)
    x = np.maximum(x, 0)
    return x.reshape(1) if x.ndim == 0 else x
