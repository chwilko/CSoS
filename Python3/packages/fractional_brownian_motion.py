import numpy as np
from alphastable import alphastable

def integral_form_simulation(N, f, dt, alpha = 0.5):
    Z = alpha_stable_levy_motion(alpha, dt, N + 1, 1)[0]
    # Z = alphastable(N, 1, alpha = alpha, beta = 0, gamma = dt ** (1 / alpha), delta = 0, k = 1)
    return f.T @ np.diff(Z)
def alpha_stable_levy_motion(alpha, dt, n, num_trajectories):
    h = dt
    M = np.zeros((num_trajectories, n))
    for i in range(num_trajectories):
        X_stable = stable(alpha=alpha, gamma=h**(1/alpha), size=n-1)
        X = np.concatenate(([0], X_stable))
        Y = np.cumsum(X)
        M[i, :] = Y
    return M
def stable(alpha: float = 2, beta: int = 0, gamma: int = 1, delta: int = 0, par: int = 0, size: int = 1) ->            np.array:
    z_0 = standard_stable(alpha=alpha,beta=beta,size=size)

    # par = 0
    if par == 0:
        if alpha == 1:
            x = gamma * z_0 + delta
        else:
            x = gamma * (z_0 - beta * np.tan(np.pi * alpha/2)) + delta

    # par = 1
    elif par == 1:
        if alpha == 1:
            x = gamma * z_0 + (delta + beta * 2/np.pi * gamma * np.log(gamma))
        else:
            x = gamma * z_0 + delta
    else:
        raise "par in {0,1}"

    return x
def standard_stable(alpha: float = 2, beta: int = 0, size: int = 1) -> np.array:
    theta = np.random.uniform(-np.pi/2, np.pi/2, size=size)
    w = np.random.exponential(scale=1, size=size)
    theta_0 = np.arctan(beta * np.tan(np.pi * alpha / 2))/alpha
    if alpha != 1:
        z_0 = np.sin(alpha * (theta_0 + theta))/(np.cos(alpha * theta_0) * np.cos(theta))**(1/alpha) * \
              ((np.cos(alpha * theta_0 + (alpha - 1) * theta))/w) ** ((1-alpha)/alpha)
    else:
        z_0 = 2/np.pi*((np.pi/2 + beta*theta) * np.tan(theta) - beta * np.log((np.pi/2 * w * np.cos(theta))
              / (np.pi/2 + beta*theta)))
    return z_0
