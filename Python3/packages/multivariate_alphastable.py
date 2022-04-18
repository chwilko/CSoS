import numpy as np
from alphastable import alphastable

def multivariate_alphastable(alpha, gamma, points):
    """function to simulate multivariate alpha stable variable
    for the discrete spectral measure

    Args:
        gamma (_type_): _description_
        points (_type_): _description_
    """
    if len(gamma) != len(points):
        raise Exception("Vectors must have the same lengths!")
    gamma = np.array(gamma).T
    points = np.array(points)
    Z = alphastable(len(gamma), 1, alpha, 1, 1, 0, 1)
    return np.sum(gamma * Z * points, 0)

