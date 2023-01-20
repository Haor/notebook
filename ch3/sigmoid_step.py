import numpy as np
import matplotlib.pyplot as plt
from sigmoid import sigmoid
from step_function import step_function


x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)

plt.plot(x,y1, label="sigmoid")
plt.plot(x,y2, linestyle = "--", label="step function")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sigmoid & step function')
plt.legend()
plt.show()