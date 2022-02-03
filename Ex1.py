import pandas as pd
#
# data={'age':[23,43,12,45,10],
#       'name':['민준','현우','서현','동현',100],
#       'height':[175.3,180.3,165.8,172.7,23]}
#
# x=pd.DataFrame(data,columns=['name','age','height'])
#
# print(x)
# print()

li1 = [[1,2,7],[3,4,8],[5,6,9]]

lx = pd.DataFrame(li1,columns=('aa','bb','cc'))

print(lx['aa'][1])
print()

print(lx.iloc[:])
print()

bools=[False,True,False]
print(lx['bb'][bools])

print(lx.mean( ))
print(lx.mean(axis=1 ))
print(lx.sum(axis=1 ))