import matplotlib.pyplot as plt

x=[0,1,2]
data=[100,200,300]  # ytick
year=['2019','2020','2021'] # xtick

plt.bar(x,data,width=0.5)
plt.xticks(x,year)

plt.show()