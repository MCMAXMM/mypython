import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,1000)
y=np.sin(x)
plt.plot(x,y)
plt.fill_between(x, 0.2, y, color="#348ABD", alpha=0.4)
plt.show()
