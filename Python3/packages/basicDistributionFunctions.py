import numpy as np
from numba import jit

from joblib import Parallel, delayed
#? basicDistributionFunctions.py

def CDF(t, X):
    length = len(t)
    MC = len(X)
    return (np.array([X.reshape(1, MC)[0] for i in range(length)]) < np.array([t for i in range(MC)]).T).sum(1) / MC

def CDF2(X):
    X = np.array(X) # Tworze nowa instancje array, inaczej zmieni sie zewnetrzny X
    X.sort(0)
    return [X, np.linspace(0, 1, X.size)]

def PDF(t, X):
    dt = (t[1] - t[0])
    t = t - dt / 2
    p = CDF(t[:-1], X)
    q = CDF(t[1:], X)
    return (q - p) / dt

def characterist_r_i(t, X):
    length = len(t)
    MC = len(X)
    X = np.array([X.reshape(1, MC)[0] for i in range(length)])
    t = np.array([t for i in range(MC)]).T
    Re = np.cos(X * t).sum(1) / MC
    Im = np.sin(X * t).sum(1) / MC
    return [Re, Im]

def tau(X, Y):
    X_ch = characterist_r_i([1], X)
    Y_ch = characterist_r_i([-1], Y)
    X_Y_ch = characterist_r_i([1], X-Y)

    X_ch = X_ch[0] +  (X_ch[1]) * 1j
    Y_ch = Y_ch[0] +  (Y_ch[1]) * 1j
    X_Y_ch = X_Y_ch[0] +  (X_Y_ch[1]) * 1j

    res = (np.log(X_Y_ch) - np.log(X_ch) - np.log(Y_ch))
    return [np.real(res)[0], np.imag(res)[0]]



def equantile(X, alpha):
    return np.sort(X, 0)[int((alpha * len(X)) // 1)]

def equantile_proces(X, alpha):
    quantiles = np.zeros(len(X[0,:]))
    for t in range(len(X[0,:])):
        quantiles[t] = equantile(X[:,t], alpha)
    return quantiles

def equantile_list(X):
    a = np.sort(X, 0)
    a[0] = 0
    return a

def characteristic_proces_r_i(x, data):
    phi = np.zeros(len(x),dtype=complex)
    for i, x_i in enumerate(x):
        p = 1 / len(data) * np.sum(np.exp(1j * x_i * data))
        phi[i] = p
    return [np.real(phi), np.imag(phi)]

@jit
def TAMSD(X, tau):
    try:
        return np.sum((X[tau:] - X[:-tau]) ** 2) / (len(X) - tau)
    except:
        return np.var(X)

@jit
def EAMSD(X, tau):
    return np.sum((X[tau,:] - X[0,:]) ** 2) / len(X[0,:])

def EATAMSD(X, tau):
    N = X.shape[1]
    # return 1 / N * np.array([TAMSD(X[:, k], tau) for k in range(N)])
    result =  Parallel(n_jobs = 8)(delayed(TAMSD)(X[:, k], tau) for k in range(N))
    return 1 / N * np.sum(result)

@jit
def TAMSD_confidence_intervals(X, taus, alpha = 0.05):
    lower = np.ones(len(taus))
    upper = np.ones(len(taus))
    val_list = np.ones(len(X))
    for i, tau in enumerate(taus):
        for k in range(len(X)):
            val_list[k] = TAMSD(X[:, k], tau)
        lower[i] = np.quantile(val_list, alpha / 2)
        upper[i] = np.quantile(val_list, 1 - alpha / 2)
    return lower, upper
