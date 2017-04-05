import os
import httplib
import json
import numpy as np
import pandas as pd
from docx import Document

in_path = 'C:\Users\NISHANT\Desktop\Sem 2\Project\DocGramCor\intermediate\data_table\students.csv'
my_cols = ['id', 'stdid', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6']
dfmain = pd.read_csv(in_path, names = my_cols, header=None, skiprows=0)
dfmain.drop(dfmain.index[[0]], inplace=True)
print dfmain.columns.values
df = pd.DataFrame()

for row in dfmain.itertuples():
    D = {}
    print row[0], row[1], row[2]
    D['stdid'] = row[2]
    merged = '. '.join(str(ele).strip('.\n\t ') for ele in row[3:])
    #merged_comment =  row[1:].str.cat(sep = '. ')
    merged_comment = merged.replace('\\', '').replace('%', ' percent')
    #merged_comment = merged.replace('%', ' percent')
    #print merged_comment
	
    document = Document()
    document.add_paragraph(merged_comment)
    document.save('Essays/'+ str(row[2]) + '.docx')
