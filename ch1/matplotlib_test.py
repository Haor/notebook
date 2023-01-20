import numpy as np
import matplotlib.pyplot as plt

#生成数据
x = np.arange(0, 6, 0.1) #以0.1为单位，生成0-6的数据
y1 = np.sin(x)
y2 = np.cos(x)
#绘制
plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle = "--", label="cos")
plt.xlabel("x") #x轴标签
plt.ylabel("y") #y轴标签
plt.title('sin & cos') #标题
plt.legend()
plt.show()
