import numpy as np

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
