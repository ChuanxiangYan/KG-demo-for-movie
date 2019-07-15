import pandas as pd
import numpy as np

df = pd.read_csv('./person_name.csv', encoding='utf-8', keep_default_na=False)
a = df.values
# b = list(a)
for i in range(len(a)):
    if a[i][0] is '':
        a[i][0] = a[i][1]
b = np.delete(a, 1, axis=1)
with open('./person_name_update.csv', 'w+', encoding='utf-8') as f:
    f.write('person_name' + '\n')
    for t in range(len(b)):
        f.write(b[t][0] + '\n')
# data = pd.DataFrame(b, columns=['person_name'], header=False, index=False)
# # print(data)
# data.to_csv('person_name_update.csv')
# print(a)
# b = a
# print(df.person_name)
# count = 0
# for i in df.person_name:
#     print(i)
# print('------------------------------')
# for i in df.person_name:
#     i
#     if i is '':
#         # i = 1
#         count += 1
# for i in df.person_name:
#     print(i)
# print(count)
# print(np.isnan(df))