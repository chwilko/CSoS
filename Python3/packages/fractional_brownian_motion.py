import numpy as np
from alphastable import alphastable

def FBM(N, t, M1 = -100, M2 = 100, I = 10000, H = 0.5, alpha = 0.5, beta = 0):
    dt = (M2 - M1) / I
    f = lambda S: np.maximum((t - S) ** (H - 1 / alpha), 0) - np.maximum((-S) ** (H - 1 / alpha), 0)
    alphastable