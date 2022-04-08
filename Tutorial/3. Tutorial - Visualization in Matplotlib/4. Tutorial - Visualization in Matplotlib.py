"""
Created on 2021

@author: Mohammad.M
"""
#Session_4
#Functions (16th Slide)
z=[1,6,4,2,8,9,0,10,11,-2];
def med(y):
 x=sorted(y);
 if len(x)%2==0:
    step=int(len(x)/2-1);
    m=(x[step]+x[step+1])/2;
 else:
    step=int(len(x)/2);
    m=x[step];
 return(m) 
med(z)

#PLot! Scatter - Hist - Bar - Pie (19th Slide)
import matplotlib.pyplot as plt;
plt.figure(figsize=(12, 8))
plt.plot(np.arange(1,10,.5),(1/3)*np.arange(1,10,.5),marker="o",c="red")
plt.scatter(np.arange(1,10,.5),(1)*np.arange(1,10,.5),marker="o",c="blue")
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

plt.figure(1)
plt.hist(np.random.normal(0,1,100))
plt.figure(2)
plt.plot(np.arange(1,100,.5),(1/3)*np.arange(101,200,.5),marker="^",c="red")
plt.xlabel('X')
plt.ylabel('Y',size = 10)
plt.show()

plt.figure(figsize=(12, 8))
plt.pie([20,15,16],explode=[0,0,0.1],labels=['Python','R','SQL'])
plt.text(-.5,.1,s='{:.1%}'.format(15/51),color="w")
plt.text(.1,.5,s='{:.1%}'.format(20/51),color="w")
plt.text(.5,-.5,s='{:.1%}'.format(16/51),color="w")
plt.show()































