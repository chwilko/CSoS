import numpy as np
import numpy.matlib
# if __name__ == "__main__":
    # from basicDistributionFunctions import *
    # import matplotlib.pyplot as plt

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


def alphastable(N, M, alpha, beta, gamma, delta, k):
    """_summary_

    Args:
        N (_type_): _description_
        M (_type_): _description_
        alpha (_type_): _description_
        beta (_type_): _description_
        gamma (_type_): _description_
        delta (_type_): _description_
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


def multivariate_alphastable_(alpha, gamma, points):
    """function to simulate multivariate alpha stable variable
    for the discrete spectral measure

    Args:
        gamma (_type_): _description_
        points (_type_): _description_
    """
    N = 1
    if len(gamma) != len(points):
        raise Exception("Vectors must have the same lengths!")
    k = len(gamma)
    gamma = np.power(np.array(gamma), 1 / alpha)
    points = np.array(points).T
    if alpha != 1:
        Z = alphastable(1, N*len(gamma), alpha, 1, 1, 0, 1)
    elif alpha == 1:
        Z = alphastable(1, N*len(gamma), alpha, 1, 1, 0, 1) + (
                2 / np.pi) * np.log(gamma)
    gamma = np.matlib.repmat(gamma, 1, N)
    points = np.matlib.repmat(points, 1, N)
    ret = gamma * Z * points
    # ret = ret.reshape((N * len(points), k)) # maybe sth is wrong in reshaping
    # ret = np.sum(ret, 1)
    # ret = ret.reshape((N, 2))
    # ret = ret.T.reshape(len(points), N).T
    return ret.sum(1)


def multivariate_alphastable(N, alpha, gamma, points):
    """function to simulate multivariate alpha stable variable
    for the discrete spectral measure

    Args:
        gamma (_type_): _description_
        points (_type_): _description_
    """
    ret = []
    for i in range(N):
        ret.append(multivariate_alphastable_(alpha, gamma, points))
    return np.array(ret)





if __name__ == "__main__":
    alpha = 0.9
    N = 10000
    gamma = [0.25, 0.125, 0.25, 0.25, 0.125, 0.25]
    points = [[1, 0], [0.5, np.sqrt(3)/2],
            [-1/2, np.sqrt(3)/2], [-1, 0],
            [-1/2, -np.sqrt(3)/2], [1/2, -np.sqrt(3)/2]] 
    print(multivariate_alphastable(N, alpha, gamma, points))
    # t = np.linspace(-3.5,3.5, 1000)
    # X = alphastable(10 ** 5,1,2,0,1 / 2 ** (1 / 2),0,1)

    # plt.figure(0)
    # plt.plot(t, CDF(t, X))

    # plt.figure(1)
    # tmp = CDF2(X)
    # plt.plot(tmp[0], tmp[1])

    # plt.figure(2)
    # plt.plot(t[:-1], PDF(t, X))

    # plt.figure(3)
    # tmp = characterist_r_i(t, X)
    # plt.plot(t, tmp[0])
    # plt.plot(t, np.exp(-t ** 2 / 2))
    # plt.figure(4)
    # plt.plot(t, tmp[1])

    # plt.show()
