import numpy as np
from scipy.stats import kstest
from matplotlib import pyplot as plt

from alphastable import alphastable


# def Levy_prcesses(M, T, dt, alpha, beta, T0=0):
def Levy_prcesses(T, M, N, alpha, beta):
    # N = (T - T0)/ dt
    S = alphastable(N, M,
        alpha, beta,
        (T/N) ** (1/alpha), 0, 1)
    S[0] = 0
    X = S.cumsum(0)
    return X


# def Levy_characteri()


if __name__ == "__main__":
    T = 1
    N = 10 ** 3
    M = 10 ** 2
    alpha = 2
    beta = 0
    X = Levy_prcesses(T, M, N, alpha, beta)
    t = np.linspace(0, 1, N)
    plt.plot(t, X)
    print(kstest(X[-1,:], 'norm'))
    plt.show()
