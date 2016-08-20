import tushare as ts
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import MyMath
hs=open('E:\data\hs300\hs300s.csv','r');
stocknum=[];
date=[];

fdate=open('E:\data\date.csv','r');
for line in fdate:
    line = line.strip();
    date = line.split(',');

count=-1;
for line in hs:
    count=count+1;
    line=line.strip();
    line=line.split(',');
    if(count>0):
        stocknum.append(line[1]);

for num in stocknum:
    if(os.path.exists('E:/data/tick/'+num)==False):
        os.mkdir('E:/data/tick/'+num);

    for day in date:
        if(os.path.exists('E:/data/tick/'+num+'/'+day+'.csv')==False):
            df = ts.get_tick_data(num, date=day);
            df.to_csv('E:/data/tick/'+num+'/'+day+'.csv');

# file=open('E:/data/time/000783/2015-09-01.csv','r');
# t=[];
# price=[];
# count=-1;
# for line in file:
#     count=count+1;
#     line=line.strip();
#     line=line.split(',');
#     if(count>0):
#         t.append(MyMath.Turntonum(line[1]));
#         price.append(line[2]);
#
# output=open('E:/data/result.csv','w');
