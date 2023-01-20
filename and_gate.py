# coding: utf-8
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2]) #将输入转换为numpy数组
    w = np.array([0.5, 0.5]) #权重
    b = -0.7 #偏置
    tmp = np.sum(w*x) + b #计算tmp
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print("AND gate")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:    #代表每一次循环xs都会取一个元组（0,0),(1,0),(0,1),(1,1)
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
#这段代码实现了一个简单的人工神经网络，它实现了一个逻辑运算"与"（AND）。
#首先，它导入了numpy库，这是一个用于科学计算的库，在这里用于数组运算。
#然后定义了一个函数AND(x1, x2)，它接受两个参数x1和x2，它们都是0或1。这个函数实现了一个线性函数，即tmp = np.sum(w*x) + b，其中w和b是网络的参数，w是权重，b是偏置。
#如果tmp小于等于0，那么函数返回0，否则返回1。这就实现了一个简单的神经元，它可以实现逻辑运算“与”。
#最后，在if name == 'main':块中，四个组合的输入参数被循环，并调用AND函数并打印结果。
