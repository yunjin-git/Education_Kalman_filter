import Kalman_filter as fl
import numpy as np
import matplotlib.pyplot as plt

i=0
dt = 0.2
time=np.arange(0,10,dt) 
Nsample = len(time)

xmsaved =np.zeros(Nsample)
Avgsaved = np.zeros(Nsample)

while i < Nsample :
    k=i+1
    xm = fl.get_static_sample(14.4,0.5)
    xmsaved[i] = xm
    if k == 1 :
        Avgsaved[0] = xm
    else:
        Avgsaved[i] = fl.Avgfilter(k,xm,Avgsaved[i-1])
    
    i=i+1

plt.plot(time,Avgsaved,"o",label = 'AvgFilter')
plt.plot(time,xmsaved,"*--", label='raw_sample')
plt.title('AvgFilter')
plt.xlabel('Time [sec]')
plt.ylabel('Volt [V]')
plt.legend(loc='upper left')

plt.show()