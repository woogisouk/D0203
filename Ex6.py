import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(30)
y=np.random.rand(30)
colors=np.random.rand(30)
shate = np.pi * (np.random.rand(30)*20)**2
plt.scatter(x,y,s=shate,c=colors,alpha=0.5)
plt.show()