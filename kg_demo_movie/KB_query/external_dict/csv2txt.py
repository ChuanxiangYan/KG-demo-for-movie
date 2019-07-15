# encoding=utf-8

"""

@author: SimmerChan

@contact: hsl7698590@gmail.com

@file: jena_sparql_endpoint.py

@time: 2017/12/20 17:42

@desc:
把从mysql导出的csv文件按照jieba外部词典的格式转为txt文件。
nz代表专名，本demo主要指电影名称。
nr代表人名。

"""
import pandas as pd

df = pd.read_csv('./movie_title.csv', encoding='utf-8', sep='\t')
title = df['movie_title'].values
# print(df.columns)
# print(df.movie_title)
with open('./movie_title.txt', 'w+', encoding='utf-8') as f:
    for t in title:
        f.write(t + ' ' + 'nz' + '\n')

df = pd.read_csv('./person_name_update.csv')
name = df['person_name'].values
with open('./person_name.txt', 'w+', encoding='utf-8') as f:
    for t in name:
        f.write(t + ' ' + 'nr' + '\n')


