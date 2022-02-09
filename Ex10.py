import matplotlib as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris)
# print(iris.describe())
plt.hist(iris['sepal_length'],bins=10)
# plt.hist(iris['sepal_length'], bins=10)
plt.show()