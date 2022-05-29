import numpy as np
from alphastable import alphastable

def f_levy(H, alpha, S, t, cut_point_1, S_negative, max_S_neg):
    cut_point_2 = np.where(S > t)[0][0] # less than t
    S_positive = S[cut_point_1 - 1:cut_point_2 - 1]
    return np.concatenate(
            ((t - S_negative) ** (H - 1 / alpha) - max_S_neg,
            (t - S_positive) ** (H - 1 / alpha))
        )

def integral_form_simulation(H = 0.3, alpha = 2, M1 = -100, M2 = 100, N_trajectories = 1, I = 10000, dt = 0.01):
    tau = (M2 - M1) / I
    S = M1 + np.arange(0, I + 1) * tau
    cut_point_1 = np.where(S > 0)[0][0] # changing sign
    S_negative = S[:cut_point_1 - 1]
    max_S_neg = np.maximum((-S_negative) ** (H - 1 / alpha), 0)
    T = np.arange(0, dt * 999, dt)
    M = np.ones((N_trajectories, len(T)))
    for i in range(N_trajectories):
        Z = alphastable(len(S), 1, alpha = alpha, beta = 0, gamma = tau ** (1 / alpha), delta = 0, k = 1)
        for j, t in enumerate(T):
            F = f_levy(H, alpha, S, t, cut_point_1, S_negative, max_S_neg)
            M[i, j] = F @ Z[:len(F)]
    return T, M
