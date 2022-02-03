import pandas as pd
import matplotlib.pyplot as plt

# drv_diy = pd.read_csv('driving.csv',engine='python',encoding='CP949')
# 
# plt.plot([1,2,3,4],[5,6,7,8],linestyle=':',marker='o')
# plt.xlabel('xx')
# plt.ylabel('yy')
# plt.axis([0,10,0,15])

x = [1,2,3,4]
y=[5,6,7,8]
plt.plot(x,y)
plt.xlabel('xx')
plt.xlabel('yy')
plt.fill_between(x[1:3],y[1:3],alpha=0.5,color='red')
plt.fill_betweenx(x[1:3],y[1:3],alpha=0.5,color='blue')
plt.fill([1.5,1.5,3.5,3.5],[2.5,4.5,2.5,4.5],alpha=0.5,color='green')
plt.show()
