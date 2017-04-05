# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 00:01:33 2016

@author: AMIT
"""
## This python module is for converting the set of .xls file into a single .csv file
wc_path = 'F:/STUDY/MTECH/2016/ProjectElective/IMPL/Experiments/intermediate/data_table/students.csv'
def create_dict(stdid, cmntlist):
    "count list dict"
    d = {}
    d['stdid'] = stdid
    i=1
    for cmnt in cmntlist:
        c = 'ans' + str(i)
        d[c] = cmnt
        i = i+1
    return d;
    
csvs = []
data_path = 'F:/STUDY/MTECH/2016/ProjectElective/InterviewData/QuestionsData/QuestionsData'
import os
for root, dirs, files in os.walk(r'F:\STUDY\MTECH\2016\ProjectElective\InterviewData\QuestionsData\QuestionsData'):
    for file in files:
    	if file.endswith('.csv'):
    		csvs.append(file)
      
import pandas as pd
import numpy as np
my_cols = ["user_id", "question_id", "idanswers", "answer", "ans1", "ans2"]
csvnames = map(lambda x: str(x[:-4]).strip().upper(), csvs)
print csvnames

df = pd.DataFrame(columns=['stdid', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6'])
for csv_file in csvs:
    print('['+csv_file+']')
    #conn = httplib.HTTPSConnection("languagetool.org")
    #conn = httplib.HTTPConnection("localhost:8082")
    data = pd.read_csv(data_path + '/' + csv_file, names=my_cols, header=None, skiprows=0)
    #comments = data.answer
    data.drop(data.index[[0]], inplace=True)
    comments = data[data.columns[3:]].apply(lambda x: ''.join(x.dropna().astype(str)), axis=1)
    
    cmntlist = []
    for comment in comments:
        if type(comment) is float:
            comment = str(comment)
        else:
            comment.strip('\n\t ')
        cmntlist.append(comment)
    stdid_name = str(csv_file[:-4]).strip().upper()
    df = df.append(create_dict(stdid_name, cmntlist), ignore_index=True)
    
print df.head(5)
df.to_csv(wc_path)