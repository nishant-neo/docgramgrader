# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 05:31:15 2016

@author: AMIT
"""

path = 'F:/STUDY/MTECH/2016/ProjectElective/IMPL/Experiments/intermediate/data_table/'
in_data = 'final3.csv'
out_data = path + 'GrammarRatings.xlsx'
#count_data = path + 'wc.csv'

import pandas as pd
import numpy as np
my_outcols = ['no', 'id', 'stdid', 'rating1', 'rating2']
dfscore = pd.read_excel(out_data, header=None, skiprows=[0,1], names=my_outcols)
df2 = pd.read_csv(in_data)

print dfscore.shape
print df2.shape
print df2.ix[:5, :2]
#df2.rename(columns={'Unnamed: 0':'stdid'}, inplace=True)

dfscore['stdid'] = dfscore['stdid'].str.strip()
df2['stdid'] = df2['stdid'].str.strip()
dfscore['stdid'] = map(lambda x: str(x).upper(), dfscore['stdid'])
df2['stdid'] = map(lambda x: str(x).upper(), df2['stdid'])
#df1.set_index('subid')
#df2.set_index('stdid')
#df_total = pd.merge(df1, df2, how='inner', left_index=True, right_index=True)
df_total = pd.merge(dfscore, df2, how='inner', on='stdid')
#df_total = pd.merge(df1, df2, how='inner', left_on='subid', right_on='stdid')
print df_total.head(5)
#df_total = pd.merge(df_total, df3_, how='inner', on='stdid')
#df_total.drop('no',1,inplace=True)
df_total['rating'] = (df_total['rating1'] + df_total['rating2'])/2
df_total['class'] = np.where(df_total['rating']>=3, 1, -1)
print df_total.head(3)
df_total.drop(['id', 'no', 'text'], axis=1, inplace=True)
col_sum_list = list(df_total)
print len(col_sum_list)
col_sum_list.remove('scount')
col_sum_list.remove('rating1')
col_sum_list.remove('rating2')
col_sum_list.remove('rating')
col_sum_list.remove('stdid')
col_sum_list.remove('wcount')
df_total['total_errors'] = df_total[col_sum_list].sum(axis=1)
print len(col_sum_list)
print df_total.head(5)
df_total.set_index(['stdid'], inplace=True)
df_total.to_csv('FeatureMatrix.csv')