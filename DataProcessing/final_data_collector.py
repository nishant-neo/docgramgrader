# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 02:00:34 2016

@author: AMIT
"""
from os import listdir
from os.path import isfile, join
import httplib
import json
import numpy as np
import pandas as pd

df = pd.DataFrame()
path = 'C:\Users\NISHANT\Desktop\Sem 2\Project\DocGramCor\Image Processing\Essays'
docs = [ f for f in listdir(path) if isfile(join(path,f)) ]    #store all image of folder
conn = httplib.HTTPConnection("localhost:8081")
for j in range(0, len(docs)):
    print join( path, docs[j])
    f = open(join( path, docs[j]) , 'r')
    merged_comment = f.read()
    
    D = {}
    print docs[j][:-4]
    D['stdid'] = docs[j][:-4]
    print merged_comment
    count= 0
  
    postData="language=en-GB&text="+merged_comment
    #conn.request("POST", "/api/v2/check", postData)
    conn.request("POST", "/v2/check", postData)
    response = conn.getresponse()
    print response.status, response.reason
    respdata = response.read()
    #print respdata
    if response.status== 200:
        json_pdata = json.loads(respdata)
        #print json_pdata
        print respdata
        with open('JSON/' + docs[j][:-4]+ '.json', 'w') as outfile:
            json.dump(json_pdata, outfile)
        for match in json_pdata["matches"]:
            rule = match["rule"]["id"]
            if rule in D:
                D[rule] += 1
            else :
                D[rule] = 1
            count += 1
    D['text'] = merged_comment
    df = df.append(D, ignore_index=True)
    print df.head()
    f.close()

conn.close()
df = df.replace(np.nan,0, regex=True)
df.to_csv('final2.csv')