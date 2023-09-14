import numpy as np
import matplotlib.pyplot as plt
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

ones = np.ones_like(X)
X_new = np.concatenate((X, ones), axis=1)
w = np.linalg.pinv(X_new.T.dot(X_new)).dot(X_new.T.dot(y))

print(w)

def predict(X):
    return X.dot(w)

x0 = np.linspace(145, 185, 2)
y0 = w[1][0] + w[0][0]*x0
plt.scatter(X, y)
plt.plot(x0, y0)              
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()