import numpy as np

def MN_distribution(N, mu, sigma):
    MN = []
    for i in range(N):
        d = 2
        a = (sigma[0][0])**(1/2)
        b = sigma[1][0] / a
        c = (sigma[1][1] - b ** 2) ** (1/2)
        L = np.array([[a, 0], [b, c]])
        Z = np.random.normal(0,1,d)
        MN.append(L @ Z + mu)
    return np.array(MN)