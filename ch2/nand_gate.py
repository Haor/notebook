import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2]) #将输入转换为numpy数组
    w = np.array([-0.5, -0.5]) #权重
    b = 0.7 #偏置
    tmp = np.sum(w*x) + b #计算tmp
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print("NAND gate")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:    #代表每一次循环xs都会取一个元组（0,0),(1,0),(0,1),(1,1)
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))