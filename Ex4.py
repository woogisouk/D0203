import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0,2,0.2)
print(data)

# plt.plot(data,data,'r--',data,data**2,'b-',data,data**3,'g:')
plt.plot(data,data,'r--')
plt.plot(data,data**2,'b-')
plt.plot(data,data**3,'g:')
plt.grid(True,axis='y',linestyle=':',alpha=0.5)
plt.show()