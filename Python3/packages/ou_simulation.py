import numpy as np
from alphastable import alphastable

def f_ou(lam, sigma, S, t):
    cut_point = np.where(S > t)[0][0] # less than t
    S_cut = S[0:cut_point - 1]
    return sigma * np.exp(-lam * (t - S_cut))

def integral_form_ou_simulation(lam = 2, sigma = 2, alpha = 2, beta = 0, M1 = -100, M2 = 100, N_trajectories = 1, I = 10000, dt = 0.01):
    tau = (M2 - M1) / I
    S = M1 + np.arange(0, I + 1) * tau
    T = np.arange(0, dt * 999, dt)
    M = np.ones((N_trajectories, len(T)))
    for i in range(N_trajectories):
        Z = alphastable(len(S), 1, alpha = alpha, beta = beta, gamma = tau ** (1 / alpha), delta = 0, k = 1)
        for j, t in enumerate(T):
            F = f_ou(lam, sigma, S, t)
            M[i, j] = F @ Z[:len(F)]
    return T, M
