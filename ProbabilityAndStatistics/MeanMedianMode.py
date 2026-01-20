import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    moy = np.mean(x)
    med = np.median(x)
    x.sort()

    count = Counter(x).most_common(1)
    mod = count[0][0]
    return float(moy), float(med), float(mod)
