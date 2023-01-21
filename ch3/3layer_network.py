import numpy as np

#这是一个三层的神经网络，输入层有2个神经元，隐藏层有3个神经元，输出层有2个神经元

def init_network():
    network = {}    #network是一个字典,它保存了每一层的权重和偏置
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])   #W1是指第一层和第二层之间的权重
    network['b1'] = np.array([0.1, 0.2, 0.3])   #b1是指第一层和第二层之间的偏置
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])  #W2是指第二层和第三层之间的权重
    network['b2'] = np.array([0.1, 0.2])    #b2是指第二层和第三层之间的偏置
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])      #W3是指第三层和第四层之间的权重
    network['b3'] = np.array([0.1, 0.2])    #b3是指第三层和第四层之间的偏置

    return network
    #权重和偏置的初始化，这里的权重和偏置是随便给的，实际上是需要通过训练来得到的


def forward(network, x):    #前向传播，封装了将输入信号转换为输出信号的过程
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1         #np.dot(x, W1)是指x和W1的矩阵乘法
    z1 = sigmoid(a1)        #sigmoid(a1)是指a1经过激活函数sigmoid后的值
    a2 = np.dot(z1, W2) + b2        #np.dot(z1, W2)是指z1和W2的矩阵乘法
    z2 = sigmoid(a2)        #sigmoid(a2)是指a2经过激活函数sigmoid后的值
    a3 = np.dot(z2, W3) + b3        #np.dot(z2, W3)是指z2和W3的矩阵乘法
    y = identity_function(a3)       #identity_function(a3)是指a3经过激活函数identity_function后的值

    return y

def sigmoid(x):    #sigmoid是指sigmoid函数
    return 1 / (1 + np.exp(-x))

def identity_function(x):   #identity_function是指恒等函数
    return x

network = init_network()
x = np.array([1.0, 0.5]) #输入层的值
y = forward(network, x) #输出层的值
print(y)    # [ 0.31682708  0.69627909]