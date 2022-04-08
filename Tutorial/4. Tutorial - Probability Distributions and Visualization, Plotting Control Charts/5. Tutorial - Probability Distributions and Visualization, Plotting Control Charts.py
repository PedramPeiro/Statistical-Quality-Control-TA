"""
Created on 2021

@author: Mohammad.M
"""

#Statistical Functions (21th Slide)
pip install scipy
from scipy.stats import bernoulli
#Normal
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
norm.rvs(loc=0, scale=1, size=1, random_state=None)
norm.cdf(3, loc=0, scale=1)
norm.pdf(1, loc=1, scale=2)
-norm.isf(0.998652, loc=0, scale=1)

x = list(range(0,100))
x = np.array(x)
x = (x/100)*6 - 3

y1 = norm.pdf(x, loc=0, scale=1)
y2 = norm.pdf(x, loc=0, scale=2)
y3 = norm.pdf(x, loc=0, scale=0.7)
plt.figure(figsize=(12, 8))
plt.scatter(x,y1,color = 'blue')
plt.scatter(x,y2, color = 'red')
plt.scatter(x,y3, color = 'pink')
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

#Exponential
from scipy.stats import expon
expon.pdf(x, loc=0, scale=1)
expon.cdf(x, loc=0, scale=1)
expon.isf(q, loc=0, scale=1)

x = list(range(0,1000))
x = np.array(x)
x = (x/1000)*10

y1 = expon.pdf(x, loc=0, scale=1)
plt.figure(figsize=(12, 8))
plt.plot(x,y1,color = 'blue',linewidth=2)
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

#Poisson
from scipy.stats import poisson
poisson.pmf(x, mu)
poisson.cdf(x, mu)
poisson.isf(q, mu)


#Session_5
#Control Chart (BoxPlot - Control Chart)
import pandas as pd
import numpy as np
df = pd.read_excel('C:/Users/cmos/Desktop/Python/EX10-Data.xlsx',encoding='latin-1')
df.iloc[:,6] = np.sum(df.iloc[:,1:6],axis=1)/5
df.iloc[:,7] = (np.max(df.iloc[:,1:6],axis=1) - np.min(df.iloc[:,1:6],axis=1))
df = df.iloc[:,1:8]
Xbar = pd.DataFrame({ 'UCL' : np.zeros(len(df)), 'CL' : np.zeros(len(df)), 'LCL' : np.zeros(len(df)) })
Rbar = pd.DataFrame({ 'UCL' : np.zeros(len(df)), 'CL' : np.zeros(len(df)), 'LCL' : np.zeros(len(df)) })

Xbar['CL'] = np.average(df.iloc[:,5])
Rbar['CL'] = np.average(df.iloc[:,6])

Xbar['UCL'] = Xbar['CL']+0.577*Rbar['CL']
Xbar['LCL'] = Xbar['CL']-0.577*Rbar['CL']

Rbar['UCL'] = 2.114*Rbar['CL']
Rbar['LCL'] = 0

df_final = pd.concat([df.iloc[:,5:7],Xbar, Rbar], axis=1)

plt.figure(figsize=(12, 8))
plt.subplot(211)
plt.plot(df_final.iloc[:,0], color = 'b' , label = 'Xbar',marker="o",alpha=0.5)
plt.title('Xbar Control Chart')
plt.ylabel('Xbar')
x_coordinates = [0, len(df_final)]
y_coordinates = [Xbar['UCL'][0], Xbar['UCL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'r')
x_coordinates = [0, len(df_final)]
y_coordinates = [Xbar['CL'][0], Xbar['CL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'y')
x_coordinates = [0, len(df_final)]
y_coordinates = [Xbar['LCL'][0], Xbar['LCL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'r')
plt.grid(linestyle='-', linewidth=0.5)
plt.subplot(212)
plt.plot(df_final.iloc[:,1], color = 'black' , label = 'Rbar', marker="o",alpha=0.5)
plt.title('Rbar Control Chart')
plt.xlabel('Number')
plt.ylabel('Rbar')
x_coordinates = [0, len(df_final)]
y_coordinates = [Rbar['UCL'][0], Rbar['UCL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'r')
x_coordinates = [0, len(df_final)]
y_coordinates = [Rbar['CL'][0], Rbar['CL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'y')
x_coordinates = [0, len(df_final)]
y_coordinates = [Rbar['LCL'][0], Rbar['LCL'][0]]
plt.plot(x_coordinates, y_coordinates,color = 'r')
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

dff = df.iloc[:,:5]
plt.figure(figsize=(12, 8))
plt.boxplot(dff)
plt.plot(np.arange(1,46),df_final.iloc[:,0], color = 'green' , label = 'Xbar',marker="o",alpha=0.9)
plt.grid(linestyle='-', linewidth=0.5)