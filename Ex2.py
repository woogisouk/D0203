import pandas as pd
#
# food = pd.read_csv('food.csv')
#
# print(food.head(5))

drv_diy = pd.read_csv('driving.csv',engine='python',encoding='CP949')

print(drv_diy)