# -*- coding: utf-8 -*-
"""
Pandas data

@author: arcji
"""
#read in file

import pandas as pd
df=pd.read_csv(r'C:\Users\arcji\Downloads\manual_elevations_experiment_data.csv',index_col='search_id')

# display max rows
pd.set_option('display.max_rows',2)


df.head()

# see no. of rows and min/max of each columsn

print(df.info())

df.shape

df.describe()

# show top 10 and bottom 10 rows

df.head(10)
df.tail(10)

#show all columns and change column name 

df.columns

df.rename(columns={"USER_ID":'USER_IxD'}, inplace=True)

#capitbalise all columns names

df.columns= [ x.upper() for x in df.columns]

#select columns 
#method 1 based on position

df.iloc[0,:]

# METHOD 2 BASED ON index and label of each 

#reset index 

df.set_index('SEARCH_ID',inplace=True)
df.reset_index(inplace=True)
df.sort_index(ascending=True)

# only select user id and user_tier

df[['USER_IxD','USER_TIER']]

# only select free tiered customers and search for cat

filt=(df['USER_TIER']=='free') & (df['QUERY'].str.contains('cat')) & (df['NUM_CLICKS'].isin([0,1]))

df.loc[filt, ['NUM_CLICKS']].head()


#replace values

# if it's free create a flag

df['free_flag']=df['USER_TIER'].str.replace({'free','yes'})

df['free_flag']=df['USER_TIER'].str.map({'free','yes'})

df.iloc[1, -1]


# replace value based 2 conditions

def used_free_search(df):
    if df['USER_TIER']=='free' and df['NUM_CLICKS']>0:
        return 'y'
    else:
        return 'n'
    
df.apply(used_free_search,axis=1)


def used_flicks(NUM_CLICKS):
    if NUM_CLICKS>0:
        return 'ye'
    else:
        return 'no'
    
df['sssss']=df['NUM_CLICKS'].apply(used_flicks)

## Create grouping 

df.groupby('sssss')[['NUM_CLICKS']].nunique

#y=df.groupby('experiment_group')[['experiment_day']].agg(["min","max"])

#get sum of number of clients and total records
df.groupby('sssss').agg({'EXPERIMENT_DAY':'count','USER_ID':'max'})

#####################
####################################

####################################
# Check null values

x=df.isna().sum()

x=1