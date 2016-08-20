import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import MyMath

hs=pd.read_csv('E:\data\hs300\hs300s.csv',encoding="gbk");
stocknum=hs['code'].tolist();
date=[];
fdate=open('E:\data\date.csv','r');
for line in fdate:
    line = line.strip();
    date = line.split(',');

for num in stocknum:
    if(os.path.exists('E:/data/tick/'+num)==True):
        for day in date:
            if (os.path.exists('E:/data/tick/' + num + '/' + day + '.csv') == True):
                data = pd.read_csv('E:/data/tick/'+num+'/'+day+'.csv', encoding="gbk");
                t = list(map(MyMath.Turntonum, data['time'].tolist()));
                price = data['price'].tolist();
                t.reverse();
                price.reverse();
                t_new = np.linspace(1, 14403, 14403);
                price_interp = np.interp(t_new, t, price);

                df2 = pd.DataFrame({'time': t_new,
                                    'price': price_interp});
                df2.to_csv('E:/data/interp/'+num+'/'+day+'.csv');



                #plt.plot(df2['time'],df2['price']);
#plt.show();

#output.write(','.join(map(str,t))+'\n'+','.join(map(str,price)));
#data=ts.get_sina_dd('600313',date='2016-06-02')
#print(data)
#data.to_csv('e:/data/dd/603822.csv');