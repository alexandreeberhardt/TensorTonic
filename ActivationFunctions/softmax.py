import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x, dtype=float)
    if x.ndim == 1:
        y = np.exp(x-np.max(x))
        total = np.sum(y)
        return y/total
    elif x.ndim == 2:
        for i in range (np.shape(x)[0]):
            x[i]=softmax(x[i])
        return x
    else : return False
    
