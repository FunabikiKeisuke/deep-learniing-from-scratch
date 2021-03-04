import numpy as np
from chapter03.sigmoid import sigmoid


def swish(x):
    return np.nan_to_num(x * sigmoid(x), nan=0.0, posinf=np.inf, neginf=-np.inf)
