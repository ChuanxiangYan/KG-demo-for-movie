import pandas as pd

data = {'name': ['Wangdachui', 'Linling', 'Niuyun'], 'pay': [4000, 5000, 6000]}
frame = pd.DataFrame(data)
frame.index = [1, 4, 5]
print(frame)
print('------------------------------------------------------')
frame['tax'] = [0.05, 0.05, 0.1]
print(frame)
print('------------------------------------------------------')
frame.iloc[1] = {'name': 'Liuxi', 'pay': 5000, 'tax': 0.05}
print(frame)
print('------------------------------------------------------')
print(frame.index)
print(frame.values)
print(frame.values.shape)
print('------------------------------------------------------')
print(frame['name'].values)


