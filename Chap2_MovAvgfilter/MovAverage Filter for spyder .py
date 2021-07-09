
import Kalman_filter as fl
import numpy as np
import matplotlib.pyplot as plt

dt = 0.2
time = np.arange(0,100,dt)
Nsample = len(time)
Avgsaved = np.zeros(Nsample)
xmsaved = np.zeros(Nsample)

i=0
n = 100

while i < Nsample :
    xm = fl.get_linear_sample(1,i,100)
    xmsaved[i] = xm
    Avgsaved[i] = fl.MovAvgfilter(i,n,xm,xmsaved)
    i=i+1
    


    
plt.plot(time,xmsaved)
plt.plot(time,Avgsaved,'*')
plt.title("MovingAvgfilter")
plt.xlabel("time[sec]")
plt.ylabel("Mearsured")
plt.show()