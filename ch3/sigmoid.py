import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x)) #这里的np.exp(-x)是指e的-x次方

X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.title('sigmoid')
plt.plot(X,Y)
plt.ylim(-0.1, 1.1) #指定y轴的范围
plt.show()
