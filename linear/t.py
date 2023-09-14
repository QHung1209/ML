import numpy as np
import matplotlib.pyplot as plt

X0 = np.array([[2], [7], [9], [3], [10], [6], [1], [8]])
Y = np.array([[13], [35], [41], [19], [45], [28], [10], [55]])
ones = np.ones_like(X0)
X = np.concatenate((X0, ones), axis=1)
m = X.shape[0]

theta_gd = np.random.normal(size=2).reshape([2,1])
learning_rate = 0.02
def grad_cal(X, Y, theta_gd, m):
    g = 1/m * X.T.dot(X.dot(theta_gd) - Y)
    return g.reshape(theta_gd.shape)
def loss(X, Y, theta_gd, m):

    return 1/(2*m) * np.sum((X.dot(theta_gd) - Y)**2)

for i in range(10000):
    grad_value = grad_cal(X, Y, theta_gd, m)
    theta_gd = theta_gd - learning_rate*grad_value
    if (i+1)%1000 == 0:
        print(loss(X, Y, theta_gd, m))

