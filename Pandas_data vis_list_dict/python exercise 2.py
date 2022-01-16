# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:39:41 2021

@author: arcji
"""
# =============================================================================
# import packages
# 
# =============================================================================
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import math  


# =============================================================================
# import data and inspect the data
# =============================================================================

df=pd.read_csv(r"C:\Users\arcji\Downloads\manual_elevations_experiment_data.csv")

df['query']=df['query'].str.upper()

x=df.groupby('query').agg({'search_id':'count'})

x.sort_values(by=['search_id'],ascending=False,inplace=True)

x.head(100)


len(df)

df['user_tier']

df.duplicated(subset=['search_id']).sum()
df[df.duplicated(subset=['search_id'])==True]
df.drop_duplicates(subset=['search_id'],keep=False,inplace=True)

df.isnull().index.sum()



df.dropna(subset=['search_id'],inplace=True)

df[df.isnull().any(axis=1)]

df.drop(index=df[df.isnull().any(axis=1)].index,inplace=True)

df.dropna(subset=['search_id'],how='any',inplace=True)

df.dropna(subset = ['column1_name', 'column2_name', 'column3_name']) 


df.loc[x.index,:]
nullrows

df.drop(index=nullrows.index,inplace=True)


filt=df['query'].str.match(r'^c')==True

filt=df['query'].str.contains('cat')==True

filt=df['query'].isin(['cat','dog'])
df.loc[filt]

df['query'].str[0:2]

df['userflag']=df['user_tier'].replace({'free':1,'paid':0})

df['userflag'].value_counts()
df['user_tier'].value_counts()

df.columns=df.columns.str.upper()

def freeuser(NUM_CLICKS):
    if NUM_CLICKS>0:
        return 1
    else:
        return 0 

df['click_flag']=df['NUM_CLICKS'].apply(freeuser)

print(df['click_flag'].value_counts())

def freepad(df):
    if (df['NUM_CLICKS']>0) & (df['USER_TIER']=='paid'):
        return 1
    elif df['NUM_CLICKS']==20:
        return 2
    else:
        return 3

df['WTH']=df.apply(freepad,axis=1)

df['WTH'].value_counts()

df.sort_values(by=['USER_ID','NUM_CLICKS'],ascending=[True,False],inplace=True)
df.head(3)      

chart_df=df.groupby(['EXPERIMENT_DAY']).agg({'SEARCH_ID':'nunique','USER_ID':'nunique'})

type(chart_df)
chart_df.reset_index(inplace=True)

chart_df.head()
from matplotlib import pyplot as plt
x=chart_df['EXPERIMENT_DAY']
y=chart_df['USER_ID']

plt.plot(x,y,color='r')

plt.title('daily search volume')
plt.xlabel('nth expriment day')
plt.ylabel('daily search volume')

plt.show()

x=df.pivot_table(index=['SEARCH_ID'],columns=['USER_ID'],
               values=['NUM_CLICKS'],aggfunc='sum')

df.drop(columns=['NUM_CLICKS'],inplace=True)

df['USER_TIER'].value_counts()

filt=df['USER_TIER']=='free'
df.drop(index=df[filt].index,inplace=True)

df.shape


dfcopy=df.copy()
dfcopy2=df

#show columns and rows in the data
df.shape
#show all the fields 
df.info()
#show all the fields 
t=df.describe()

# =============================================================================
# check missing varibales and duplicates
# 
# =============================================================================

df.isnull().sum()
filt=df.isnull()
# drop rows with null query values 
df.drop (index=df[filt].index,inplace=True)

#drop duplicated rows 
dfcopy.duplicated(subset=['search_id']).sum()
dfcopy.drop_duplicates(subset=['search_id'],keep=False, inplace=True)


# =============================================================================
# change the data column names
# =============================================================================

dfcopy.columns
dfcopy.rename(columns={'search_id':'SEARCHID'},inplace=True)
dfcopy.columns=dfcopy.columns.str.replace("_","")
dfcopy.columns=dfcopy.columns.str.upper()

dfcopy.head()
# =============================================================================
# reset index
# =============================================================================

dfcopy.set_index('SEARCHID',inplace=True)
dfcopy.sort_index(ascending=False)
dfcopy.reset_index(inplace=True)
dfcopy.head(1)

# =============================================================================
# get top 10 rows and first column in the data
# =============================================================================

dfcopy.iloc[1:10,5]
dfcopy.loc[0:2,['QUERY']]

# =============================================================================
# #filtering
# =============================================================================

filt=(df['query'].str.contains('c',na=False))
df.loc[filt]

filt=(df['query'].isin(['cat','dog']))
df.loc[filt]

filt=(df['query']=='cat')
df.loc[filt]

filt=(df['query'].str.match(r'(^c)',"i")==True)
df.loc[filt]


# =============================================================================
# replace values 
#       
# =============================================================================
df.columns

def clickflag(num_clicks):
    if num_clicks>0:
        return 1
    else:
        return 0

df['click_flag']=df['num_clicks'].apply(clickflag)

def click_free(df):
    if (df['num_clicks']>0) & (df['user_tier']=='free'):
        return 1
    else:
        return 0
df['clickfree_flag']=df.apply(click_free,axis=1)

df['clickfree_flag'].value_counts()

