import numpy as np
from basicDistributionFunctions import characterist_r_i, CDF2

if __name__ == "__main__":
    from basicDistributionFunctions import *
    import matplotlib.pyplot as plt


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
    try:
        U = np.pi * (np.random.rand(N, M) - 1 / 2)
        W = -1 * np.log(np.random.rand(N, M))
    except TypeError:
        print("Warrning: alphastable_ in alphastable.py")
        print("        U = np.pi * (np.random.rand(N, M) - 1 / 2)")
        print(f"N and M should be int not {type(N)} and {type(M)}")
        U = np.pi * (np.random.rand(int(N), int(M)) - 1 / 2)
        W = -1 * np.log(np.random.rand(int(N), int(M)))

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

def multivariate_alphastable(alpha, gamma, points, N = 1):
    """function to simulate multivariate alpha stable variable
    for the discrete spectral measure

    Args:
        gamma (_type_): _description_
        points (_type_): _description_
    """
    Random_vector = np.ones((N, 2))
    if len(gamma) != len(points):
        raise Exception("Vectors must have the same lengths!")
    gamma = np.array(gamma)
    gamma = np.power(gamma, 1/alpha)
    points = np.array(points).T
    Z = alphastable(N, len(gamma), alpha, 1, 1, 0, 1)
    for i in range(N):
        Random_vector[i, :] =  np.sum(gamma * Z[i, :] * points, 1)
    return Random_vector

def get_alpha_char(alphastable_vector, t):
    """Function performing the linear regression algorithm for
    finding the alpha parameter of alpha stable sample.

    Args:
        alphastable_vector (_type_): _description_
        t (_type_): _description_

    Returns:
        _type_: _description_
    """    
    Re_char_X = characterist_r_i(t, alphastable_vector)[0] # instead of Re you can take Abs
    Y = np.log(-np.log(np.abs(Re_char_X))).T
    X = np.vstack((np.log(t), np.ones(len(Y)))).T
    alpha, beta = np.linalg.inv(X.T @ X) @ X.T @ Y
    return alpha, beta

def get_alpha_cdf(alphastable_vector, perc):
    """Function performing the linear regression algorithm for
    finding the alpha parameter of alpha stable sample.

    Args:
        alphastable_vector (_type_): _description_
        perc (_type_): _description_

    Returns:
        _type_: _description_
    """    
    N = len(alphastable_vector)
    [sorted_X, ecdf] = CDF2(alphastable_vector)
    ecdf_cut = ecdf[-int(perc * N):-1]
    X_cut = sorted_X[-int(perc * N):-1]
    Y = np.log(1 - ecdf_cut)
    X = np.vstack((np.log(X_cut), np.ones(len(X_cut)))).T
    alpha, beta = np.linalg.inv(X.T @ X) @ X.T @ Y
    return -alpha

if __name__ == "__main__":
    t = np.linspace(-3.5,3.5, 1000)
    X = alphastable(10 ** 5,1,2,0,1 / 2 ** (1 / 2),0,1)

    plt.figure(0)
    plt.plot(t, CDF(t, X))
    print("figure(0)")

    plt.figure(1)
    tmp = CDF2(X)
    plt.plot(tmp[0], tmp[1])
    print("figure(1)")

    plt.figure(2)
    plt.plot(t[:-1], PDF(t, X))
    print("figure(2)")

    plt.figure(3)
    tmp = characterist_r_i(t, X)
    plt.plot(t, tmp[0])
    plt.plot(t, np.exp(-t ** 2 / 2))
    print("figure(3)")

    plt.figure(4)
    plt.plot(t, tmp[1])
    print("figure(4)")

    plt.show()
