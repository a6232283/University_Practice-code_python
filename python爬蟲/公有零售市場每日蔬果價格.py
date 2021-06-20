import numpy as np
import pandas as pd
import seaborn as sbn
from matplotlib import pyplot as plt

# plt.style.use('ggplot')
# plt.rcParams['font.sams-serif']=['SimHei']

df=pd.read_csv('公有零售市場每日蔬果價格.csv')
# print(df.info())
# print(df)

#數據清洗
df.drop(columns='市場名稱',inplace=True)

#檢查重複數據
df.duplicated().sum()

#缺失處裡
df.isnull().sum()

#標準化處理
df['Date']=pd.to_datetime(df['Date'] , format="%d/%m/%Y")

#分析階段 按月分析
df['Moth']=df.Date.astype('datetime64[M]')
group_Month=df.groupby('Moth')
t=group_Month['午仔魚','吳郭魚','龍虎班'].sum()
print(t)

print(df)