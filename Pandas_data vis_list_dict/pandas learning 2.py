# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:57:06 2021

@author: arcji
"""

import pandas as pd 

df=pd.read_csv(r'C:\Users\arcji\Downloads\manual_elevations_experiment_data.csv')

pd.set_option('display.max_rows',20)

#Basic data information

df.shape #how many rows/colums
df.info() #show basic data field attributes
type(df.describe())

#captilize all the columns

df.colums=[x.upper() for x in df.columns]

#change experiment_day to date
df.rename(columns={'experiment_day':'exp_day'},inplace=True)

df.columns=df.columns.str.upper()

#calculate duplicated columns
# the exact same rows
df.duplicated().sum()

df.duplicated(subset=['SEARCH_ID']).sum()
df.duplicated(subset=['USER_ID']).sum()

# =============================================================================
# 6. Removing Duplicate Records in the Dataset.
# 
# =============================================================================
df.drop_duplicates(keep = 'first')


#####
df1=df.copy()
### 

# =============================================================================
# identify missing columns
# =============================================================================
df.isnull().sum()
#get null colums

df.loc[df['QUERY'].isnull(),:]

#############
## identify 

# =============================================================================
# select rows and columns
# =============================================================================


df.iloc[0:1,2:5]

df.loc[2:6,['USER_ID','USER_TIER']]

df[['USER_ID','USER_TIER']]

# =============================================================================
# FLTER
# =============================================================================

#select free and expriment day=10

df['USER_TIER'].value_counts(normalize=True)

filt=(df['USER_TIER']=='free') & (df['EXP_DAY']==10)

df[filt]
#add date to expreiment date

filt=(df['SEARCH_ID'].isin(['XUPtQjdW','HDGbOSLz']))
df[filt]

filt=(df['SEARCH_ID'].str.contains('XUP'))
df[filt]

#CREATE A NEW FIELD BASED ON EXISTING ONE

df['free_flag']=df['USER_TIER'].map({'free':'Y'})
df['free_flag']=df['USER_TIER'].replace({'free':'Y'})

def bin_exper_day(experiment_day):
    if experiment_day <= 20:
        return 'less than 20'
    else:
        return 'over than 20'

df['xxx']=df['EXP_DAY'].apply(bin_exper_day)

def free_exp(df):
    if (df['experiment_day'] <= 20)  & (df['user_tier']=='FREE'):
        return 'xx'
    else: 
        return 'yy'

df['xxxx']=df.apply(free_exp,axis=1)


# =============================================================================
# SORT VALUES BY PLICE 
# 
# =============================================================================

df.sort_values(by=['EXP_DAY','SEARCH_ID'],ascending=[True,False],inplace=True)

# drop columns
df.drop(columns=['x','index'],inplace=True)

# drop rows
filt=df['search_id']=='AOGFabmo'
df.drop(index= df[filt].index,inplace=True)

# concencatnate
df['y']=df['search_id']+' ' +df['user_id']
df[['y1','y2']]=df['y'].str.split(' ',expand=True)


df['index'].nlargest(10)
df.nlargest(10,'experiment_day')


df.groupby('experiment_group')['experiment_day'].agg(['median','max'])


df.isna().sum()
df.dropna(axis='index', how='any') 
df.fillna('MISSING')

df.replace({'MISSING':np.nan},inplace=True)

df['query'].fillna(mean)


from datetime import datetime, timedelta

initial_dt=datetime(2020,12,31)

exp_dtlist=[]

exp_day=pd.DataFrame(df.groupby('EXP_DAY'))[0].to_list()

for i in exp_day: 
    exp_dtlist.append(initial_dt+timedelta(days=i))
    
#creaet date reference data
exp_dtref={'EXP_DAY':exp_day,'EXP_DATE':exp_dtlist}    
exp_dttable=pd.DataFrame(exp_dtref)

pd.merge(df,exp_dttable,left_on='EXP_DAY',
         right_on='EXP_DAY',how='left')

df.info()


# =============================================================================
# dattime exercises in Pandas
# =============================================================================


tstdt=datetime(2020,12,31)
#add a few days
tstdt+ timedelta(days=1)

#convert a pandas string to date
df['fixed_dt']='2021-01-01'
df['fixed_dt']= pd.to_datetime(df['fixed_dt'],format='%Y-%m-%d')

#add 2 days to fixed dates
df['fixed_dt']= df['fixed_dt'] + pd.Timedelta(days=10)

df['fixed_dt']= df['fixed_dt'] + pd.to_timedelta(df['EXP_DAY'], unit='D')

# =============================================================================
# ###
# #regular expression on pandas 
# 
# =============================================================================

## fitler all data starting with x

import re

filt=(df['QUERY'].str.match(r'(^r.*)')==True)
filt=(df['SEARCH_ID'].str.match(r'(^a.*)')==True)
df[filt]

## Get first 2 s
#Extract the first 2 characters of each country using ^(
df['first_five_Letter']=df['QUERY'].str[0:2]
df.head()

#remove 1 or more spaces in the text 
df.replace(r"^ +| +$", r"", regex=True, inplace=True)

# get the countries starting with character ‘F’. 
S=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
S[S.str.count(r'(^F.*)')==1]

###
dix['sss']=pd.to_numeric(dix['sss'],errors='coerce')
dix['sss']=dix['sss'].astype('numeric')


#UNILL 2 TABLES
df_union_all= pd.concat([df1, df2],ignore_index=True)


# =============================================================================
# # =============================================================================
# # def add_days(df):
# #     df['EXP_DT']=df['EXP_DT']+ pd.Timedelta(days=df['EXP_DAY'])
# # 
# # df.apply(add_days,axis=1)
# # =============================================================================
# 
# =============================================================================

x=df.groupby('experiment_day')[['search_id']].agg(["nunique"])
x.columns

