import sys
import numpy as np
from scipy.stats import kstest
from matplotlib import pyplot as plt


from packages.alphastable import alphastable


def Levy_processes(T, M, N, alpha, beta):
    """_summary_

    Args:
        T (_type_): Finish time of process. (Probably not the best name)
        M (_type_): Number of independend proceses.
        N (_type_): Number of times steps.
        alpha (_type_): alpha parameter for Levy Proceses.
        beta (_type_): beta parameter for Levy Proceses.

    Returns:
        np.array: Levy proceses 
    """    
    S = alphastable(N, M,
        alpha, beta,
        (T/N) ** (1/alpha), 0, 1)
    S[0] = 0
    X = S.cumsum(0)
    return X




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
