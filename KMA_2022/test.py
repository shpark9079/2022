# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:20:48 2021

@author: shpark
"""

import pandas as pd

base_dir='c:/Users/shpark/OneDrive/2021/ETC/'

df=pd.read_csv(base_dir+'aws_114_20140107.txt',header=None)

aa=[];time=[]
for i in range(len(df)):
    line=str(df.iloc[i].to_list()[0]).split(' ')
    
    if (len(line) == 8):
        aa.append(line)
        yy=line[0][0:4]
        mm=line[0][4:6]
        dd=line[0][6:8]
        hh=line[0][8:10]
        minu=line[0][10:12]
        tt=yy+'-'+mm+'-'+dd+' '+hh+':'+minu+':00'
        time.append(tt)
        
    
df1=pd.DataFrame(aa)    
date=pd.to_datetime(time)
df1.columns=['date','loc','lon','lat','1','2','3','4']
df1.set_index(date,inplace=True)
df1=df1.drop(['date'],axis=1)
df1.index.name='date'

df1.to_csv(base_dir+'/test1111.csv')
