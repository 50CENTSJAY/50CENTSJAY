# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:39:39 2021

@author: arcji
"""
# Import all the packages

from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np 


# set up mock-up datasets
x1=np.array(list(range(10)))
x2=x1-5
y=x1+2


#chosse chart style
#print(plt.style.available)

#pick a chart style
plt.style.use('seaborn-paper')

# create a line chart 
plt.plot(x1,y,c='b',marker='*',linestyle='--',label='x1')
plt.plot(x2,y,c='r',label='x2',linewidth=3)

plt.title('Daily trend')
plt.xlabel('trend1')
plt.ylabel('y-axis')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

#create a stack bar chart 

x=np.array(list(range(10)))+5
y1=x+2
y2=x+3
y3=x+3

#chart contents
plt.bar(x,y1,color='b',label='x1')
plt.bar(x,y2,color='r',bottom=y1,label='x2')
plt.bar(x,y3,color='r',bottom=y1+y2,label='x3')

#style of the chart 
plt.title('bar chart')
plt.title('bar chart')

plt.show()

#create 
xaxis=np.arange(len(x))
width=0.3

plt.bar(xaxis,y1,width=width,label='x1')
plt.bar(xaxis+width,y2,width=width,label='x2')

plt.xticker(ticks=xaxis,label=x)
plt.title('comparions chart')

plt.legend()

plt.show()


# create a vertical bar chart

plt.barh(x,y1,color='b')


# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
  
# create data
df = pd.DataFrame([['A', 10, 20, 10, 26], ['B', 20, 25, 15, 21], ['C', 12, 15, 19, 6],
                   ['D', 10, 18, 11, 19]],
                  columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
# view data
print(df)
  
# plot data in stack manner of bar type
df.plot(x='Team', kind='bar', stacked=True,
        title='Stacked Bar Graph by dataframe')




# plot bars in stack manner
plt.stackplot(x,y1,y2)

plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Round 1", "Round 2", "Round 3"],loc='upper left')
plt.title("Scores by Teams in 4 Rounds")
plt.show()


# creata histgram
plt.hist(x,bins=10,edgecolor='w')
plt.axvline(np.median(x),color='red')
plt.show()

#scatter 
plt.scatter(x,y1,s=y2,cmap='summer',c='green')

#create color bar on the side
cbar=plt.colorbar()
cbar.set_label('ssds')

#chart title and labels
plt.title('chart1')
plt.xlabel('daily1')
plt.xlabel('daily2')


#create 2 plots 
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y1)
axs[1].plot(x, y2)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('Aligning x-axis using sharex')
ax1.plot(x, y1)
ax2.plot(x + 1, y2)


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x, y1)
ax2.plot(x, y2)