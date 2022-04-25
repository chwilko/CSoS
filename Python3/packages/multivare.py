import numpy as np

from basicDistributionFunctions import tau

def MN_distribution_old(N, mu, sigma):
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

def MN_distribution(N, mu, Sigma):
    MN = []
    for i in range(N):
        L = Cholesky_factor(Sigma)
        d = len(mu)
        Z = np.random.normal(0,1,d)
        MN.append(L @ Z + mu)
    return np.array(MN)


def Cholesky_factor(Sigma):
    '''
        Sigma -- Symmetric matrix
    '''
    n = len(Sigma)
    L = np.zeros((n,n))
    for i in range(n):
        for j in range(i, n):
            if j == i:
                L[i,j] = (Sigma[i][j]
                    - sum([L[k][i] * L[k][j] for k in range(i)])) ** (1/2)
            else:
                L[i,j] = (Sigma[i][j]
                    - sum([L[k][i] * L[k][j] for k in range(i)]))/ L[i][i]
    return np.array(L).T



def multivate_characteristic_r_i(T, X):
    # '''
    #     Tau -- list of meshgrids
    # '''
    return multivate_characteristic_r_i_2_dim(T,T,X)


def multivate_characteristic_r_i_2_dim(T1, T2, X):
    # '''
    #     Tau -- list of meshgrids
    # '''
    Re = np.ones((len(T1), len(T2)))
    Im = np.ones((len(T1), len(T2)))
    for i in range(len(T1)):
        for j in range(len(T2)):
            Re[i, j] = np.sum(np.cos(T1[i] * X[:, 0] + T2[j] * X[:, 1]))
            Im[i, j] = np.sum(np.sin(T1[i] * X[:, 0] + T2[j] * X[:, 1]))
    return [Re / len(X), Im /len(X)]


# def multivate_characteristic(Tau, X):
#     '''
#         Tau -- list of meshgrids
#     '''
#     T = np.zeros(Tau[0].shape)
#     N = len(X)
#     for i in range(len(Tau)):
#         for k in range(N):
#             T[i] += Tau[i] * X[k][i]
#     T = T / N
#     return np.exp(1j * T)


def tau_2_dim(X):
    X = np.array(X)
    return tau(X[:,0], X[:,1])
    

if __name__ == "__main__":
    A_ = []
    A_.append(np.array([[1,1/2], [1/2,4]]))
    A_.append(np.array([[1,1/2, 1/3], [1/2,4, 1/4], [1/3, 1/4, 3]]))

    for A in A_:
        L = Cholesky_factor(A)
        print(L)
        print("Powinno być 0: ", (A - L @ L.T).sum())
        print()
        print()
