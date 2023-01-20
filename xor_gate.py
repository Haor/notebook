from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1, x2): #XOR gate
    s1 = NAND(x1, x2) #s1 = NOT(AND(x1, x2))
    s2 = OR(x1, x2) #s2 = OR(x1, x2)
    y = AND(s1, s2) #y = AND(s1, s2)
    return y

if __name__ == '__main__':
    print("XOR gate")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:    
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

# XOR gate是一个非线性的逻辑电路，因此无法用单层感知机来实现
# 但是可以用多层感知机来实现
# Path: xor_gate2.py