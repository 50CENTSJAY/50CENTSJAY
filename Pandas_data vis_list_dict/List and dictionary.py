# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:02:05 2021

@author: arcji
"""

"""
String opeartors 
Learning guide

"""
# make a string 
a='xxx'
b='yyy'
# append a string
print(a+b)

# upper or lower cases
b.lower()
b.upper()

# show the escape of a string
c='i HEART \'SSS\'' 

# remove character of a characters 
c.strip("'")

# replace a characters
c.replace('S','DD')

#split a string to list
c.split(" ")

#join a list to a string
d=['222','232131','2131231321']

t=(":").join(d)

t

"""
List operators
###########
"""

a=[1,2,3,4]
b=[2,324,235]

#combine 2 list 
c=a+b


#select top 5 elemets
print(c[0:5])

#select last 2 elements
print(c[-2:])
#select all but last 2 elements
print(c[:-2])

#add new elements
c.append([2,2,3])

#remove element
c.pop() #remove last one

c.pop(2) # remove the xth element

c.remove(1) 

# count occurence of an element
c.count(2)

#sort 
sorted(c,reverse=True )

# use range to create dummy data

x=list(range(9))
x



for i in x:
    print(x)
    
for l,i in enumerate(x):
    print (l,i)


"""
Dictionary
###########
"""

d={}
d['qqw']=1
d['qqwxx']=2

# change vlaues o a key

d['qqw']='tt'

d.keys()
d.values()

#for loop iterates 

for key,value in d.items():
    print(key,value)
    
"word count  "

txt='i lsio i sliol w,e abadio'

lxx=txt.split(" ")


counter={}

for t in lxx: 
    if t in counter:
        counter[t]+=1
    else:
        counter[t]=1
        
