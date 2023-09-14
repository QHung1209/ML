import numpy as np
import matplotlib.pyplot as plt

X_old = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

ones = np.ones_like(X_old)
X = np.concatenate((X_old, ones), axis=1)
m = X.shape[0]

learning_rate = 0.0001
theta_gd = np.random.normal(size=2).reshape([2,1])
def grad(X, y, theta_gd, m):
    g = 1/m * X.T.dot(X.dot(theta_gd) - y)
    return g.reshape(theta_gd.shape)

def loss(X, y, theta_gd, m):
    j = 0.5*m*np.sum((X.dot(theta_gd) - y)**2)
    return j

for i in range(10000000):
    grad_value = grad(X, y, theta_gd, m)
    theta_gd = theta_gd - learning_rate*grad_value

print(theta_gd)

x0 = np.linspace(145, 185, 2)
y0 = theta_gd[1][0] + theta_gd[0][0]*x0
plt.scatter(X_old, y)
plt.plot(x0, y0)              
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()