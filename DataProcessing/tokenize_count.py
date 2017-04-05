# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 04:03:26 2016

@author: AMIT
"""
#this python module adds up the token and the sentence count of the essays
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import *
in_path = 'final2.csv'

def func(text):
    scount = wcount = 0
    st = sent_tokenize(text)
    scount = len(st)
    for t in st:
        wt = word_tokenize(t)
        wcount += len(wt)
    return pd.Series({'scount': scount, 'wcount': wcount})

def swcounter(s):
    text = s['text']
    scount = wcount = 0
    print text
    st = sent_tokenize(text.decode('utf-8'))
    scount = len(st)
    for t in st:
        print t
        wt = word_tokenize(t)
        wcount += len(wt)
    s['scount'] = scount
    s['wcount'] = wcount
    print "DONE!!!!!!!!!!!!!!!!!!!!!!!!!"
    return s
    
dfmain = pd.read_csv(in_path)
#, names = my_cols, header=None, skiprows=0)
print dfmain.columns.values
print dfmain.shape

#dfmain['scount'], dfmain['wcount'] = dfmain['text'].apply(lambda x: func(x))
dfmain = dfmain.apply(swcounter, axis=1)
print dfmain.shape
dfmain.drop(['Unnamed: 0'], axis=1, inplace=True)
dfmain.set_index(['stdid'], inplace=True)
dfmain.head(2)
print dfmain.shape
dfmain.to_csv('final3.csv')