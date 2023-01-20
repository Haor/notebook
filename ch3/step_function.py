import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int) #将布尔值转换为整数

x = np.arange(-5.0, 5.0, 0.1) #以0.1为单位，生成-5.0-5.0的数据
y = step_function(x)
plt.title('step function')
plt.plot(x,y)
plt.ylim(-0.1, 1.1) #指定y轴的范围
plt.show()