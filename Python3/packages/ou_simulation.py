import numpy as np
from numba import jit

@jit
def f_ou(lam, sigma, S, t):
    cut_point = np.where(S > t)[0][0] # less than t
    S_cut = S[0:cut_point - 1]
    return sigma * np.exp(-lam * (t - S_cut))

def integral_form_ou_simulation(lam = 2, sigma = 2, alpha = 2, beta = 0, M1 = -100, M2 = 100, N_trajectories = 1, I = 10000, dt = 0.01, time_horizon = 999):
    tau = (M2 - M1) / I
    S = M1 + np.arange(0, I + 1) * tau
    T = np.arange(0, dt * time_horizon, dt)
    M = np.ones((len(T), N_trajectories))
    for i in range(N_trajectories):
        Z = alphastable(len(S), 1, alpha = alpha, beta = beta, gamma = tau ** (1 / alpha), delta = 0, k = 1)
        for j, t in enumerate(T):
            F = f_ou(lam, sigma, S, t)
            M[j, i] = F @ Z[:len(F)]
    return T, M

@jit
def alphastable_(N, M, alpha, beta):
    """_summary_

    Args:
        N (_type_): _description_
        M (_type_): _description_
        alpha (_type_): _description_
        beta (_type_): _description_

    Returns:
        _type_: _description_
    """
    U = np.pi * (np.random.rand(N, M) - 1 / 2)
    W = -1 * np.log(np.random.rand(N, M))

    if alpha == 1:
        X = 2 / np.pi * (
            (np.pi / 2 + beta * U) * np.tan(U) - 
            beta * np.log(W * np.cos(U) / (1 + (2 / np.pi) * beta * U))
        )
    else:
        B = (np.arctan(beta * np.tan(np.pi * alpha / 2))) / alpha
        S = (1 + beta ** 2 * (np.tan(np.pi * alpha / 2)) ** 2) ** (1 / (2 * alpha))
        X = S * (np.sin(alpha * (U + B))) / ((np.cos(U)) ** (1 / alpha)) * ((np.cos(U - alpha * (U + B))) / W) ** ((1 - alpha) / alpha)
    return X

@jit
def alphastable(N, M, alpha, beta, gamma, delta, k):
    """_summary_

    Args:
        N (_type_): _description_
        M (_type_): _description_
        alpha (float): must be between 0 and 2 (excluding 0 and including 2)
        beta (float): between -1 and 1
        gamma (float): greater or equal zero
        delta (float): real number
        k (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if k == 0:
        if alpha == 1:
            X = gamma * alphastable_(N, M, alpha, beta) + delta
        else:
            X = gamma * (alphastable_(N, M, alpha, beta) - beta * np.tan(np.pi * alpha / 2)) + delta
    else:
        if alpha == 1:
            X = gamma * alphastable_(N, M, alpha, beta) + (delta + beta * 2 / np.pi * gamma * np.log(gamma))
        else:
            X = gamma * alphastable_(N, M, alpha, beta) + delta
    return X

