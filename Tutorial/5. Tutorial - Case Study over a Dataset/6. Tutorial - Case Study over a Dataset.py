"""
Created on 2021

@author: Mohammad.M
"""

#Session_6 (25th Slide)
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/cmos/Desktop/Python/googleplaystore3-1.csv',na_values=' ')
#'''
df.describe(include="all")
df.dtypes
df.head(3)
df.tail(3)
df.shape
df.columns

df.isna()
df['Reviews']
df.iloc[:,4]
df.loc[:,'Reviews']
df1=df.loc[:,['Rating','Reviews']]#Make a new dataframe with Rating and Reviews variables 
df1=df.iloc[:,[3,4]]
df['Reviews'].isna()#Finding the missing values in Reviews
sum(df['Reviews'].isna())
df['Type'].unique()#find the levels of variable Type

df.index[df['Reviews'].isna()]#Find the Reviews missing values
np.where(df['Reviews'].isna())#same
df.index[df['Rating']>4.9]#Find the rows with Ratings larger than 4.9
sum(df['Rating']>4.9)
Reviews=df.loc[df['Rating']>4.9,'Reviews']#Find the Reviews for apps with Rating larger than 4.9
type(df)
Reviews_lowrate=df.loc[df['Rating']<3.5,'Reviews']#Find the Reveiews for Ratings less than 3.5

df1=df.iloc[:,[3,4]]
df1.agg(np.mean,axis=0)#.agg(fun,axis) applies a function to rows or columns of a dataframe.Compute the mean of each variable (each column) 
df1.agg(np.sum,axis=1)
df1.agg(['sum','min','max'])#Applies two functions on both variables 

'Group the dataframe'
df.loc[df['Type'].isna(),'Type']='Not Available'
np.unique(df['Type'])#Get the levels
df2=df.groupby('Type')


df2.agg({"Rating":['mean','std']})#Compute the mean and standard deviation of Rating for each level of variable Type
df3=df2.agg({"Rating":['mean','std'],"Reviews":['mean','std']})
df2.get_group('Free')


'Multi index dataframe'
df3.iloc[:,1]
df3.columns
df3.loc[:,('Reviews', 'std')]#Call one column using its name
df3.loc['Free',('Reviews', 'std')]#Call an element using its row and column names

df.dropna(axis=0,inplace=True)#Delete the missing values

df5=df.groupby('Category').agg({"Reviews":['mean'],'Rating':['mean']})#Group by categpry and compute the mean of Reviews and Rating 
df6=df5.sort_values(('Reviews','mean'),ascending=False)#sort the dataframe based on the Reviews
df6=df6.iloc[0:10,:]


'plot a histogram for Rating' 
plt.hist(df['Reviews'].dropna(),30, facecolor='g',edgecolor="r")

Rew_Norm = df['Reviews'].loc[df['Reviews']<5000].dropna()
plt.hist(Rew_Norm, 30, facecolor='g',edgecolor="r")
    

import numpy as np 
import statsmodels.api as sm 
import pylab as py 
  
# Random data points generated 
data_points = np.random.normal(0, 1, 100)     
  
sm.qqplot(data_points, line ='45') 
py.show()


'Plot a pie chart for mean of reviews'
exp=np.zeros(10)
exp[0]=0.2
plt.pie(df6[('Reviews','mean')],labels=df6.index,explode=exp)

'Plot a viplinplot for Rating'
plt.violinplot(df['Rating'].dropna(),showmedians=True)


'Plot a barchart for number of apps in a category'
df7=df.groupby('Category')
plt.bar(df7.count().index,df7.count().App)
plt.xticks(np.arange(0,33),df7.count().index,rotation=90)#Rotate the text to make it vertical

'plot the histogram of Reviews and Review2 on the same plot.
fig=plt.figure()#Define a figure
ax1=fig.add_axes([0,0,1,1])#Give the location of the major plot 										    
ax2=fig.add_axes([0.2,0.65,0.4,0.2])#Specify the location of the second plot										    
ax1.hist(Reviews_lowrate.dropna(), 30, facecolor='g',edgecolor="r")
ax2.hist(Reviews.dropna(), 30, facecolor='b',edgecolor="r")
plt.show()

'make a list of Rating for each category as a component in the list'
l=[]
for x in np.unique(df['Category']):
    l.append(df['Rating'].loc[df['Category']==x].dropna())
plt.boxplot(l,notch=True)
plt.xticks(np.arange(1,34),np.unique(df['Category']),rotation=90)
plt.axhline(np.mean(df['Rating']),color='red')

plt.scatter(df['Reviews'],df['Rating'],marker="o",c="red")
h=[]
for x in np.unique(df['Type']):
    h.append(df['Rating'].loc[df['Type']==x].dropna())
plt.boxplot(h,notch=True)
plt.xticks(np.arange(1,4),np.unique(df['Type']),rotation=90)


#END!!!!!!!!