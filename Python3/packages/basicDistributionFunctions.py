import numpy as np
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
    return np.sort(X, 0)[alpha * len(X) // 1]

def equantile_list(X):
    a = np.sort(X, 0)
    a[0] = 0
    return a