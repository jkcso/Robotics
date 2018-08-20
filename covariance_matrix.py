import numpy as np

def covariance_matrix(x, y):
    p = np.array([[0.0, 0.0], [0.0, 0.0]])
    p[0][0] = np.var(x)
    p[0][1] = sumxy(xs, ys) / len(x)
    p[1][0] = p[0, 1]
    p[1][1] = np.var(y)
    return p

def sumxy(x, y):
    meanx = np.mean(xs)
    meany = np.mean(ys)
    sum = 0
    for i in range(len(xs)):
        sum += (x[i] - meanx) * (y[i] - meany)
    return sum

N = 10
# xs = np.array([0] * N)
# ys = np.array([0] * N)
xs = [0, -0.2, -0.5, -1.1, -1.3, -2.1, 2.0, -2.3, 1.0, 1.1]
ys = [2.4, 3.3, 2.3, 2.8, 3.4, 3.2, 4.2, 4.9, 1.1, 1.7]
p = covariance_matrix(xs, ys)
print p[0][0], p[0][1]
print p[1][0], p[1][1]
