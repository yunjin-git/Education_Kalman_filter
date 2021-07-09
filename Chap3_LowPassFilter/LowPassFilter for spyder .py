import Kalman_filter as fl
import numpy as np
import matplotlib.pyplot as plt

dt = 1
time = np.arange(0,100,dt)
Nsample = len(time)
prevx = np.zeros(Nsample)
xmsaved = np.zeros(Nsample)
alpha = 0.9
i=0
while i < Nsample :
    xm = fl.get_linear_sample(1,i,100)
    xmsaved[i] = xm
    
    if k == 1 :
        prevx[0] = xm
    else:
        prevx[i] = fl.LPF(alpha,xm,prevx[i-1])
    i=i+1

plt.plot(time,prevx,"-",label = 'LowPassFilter')
plt.plot(time,xmsaved,"-", label='raw_sample')
plt.title('AvgFilter Error')
plt.xlabel('Time [sec]')
plt.ylabel('Measured [V]')
plt.legend(loc='lower right')

plt.show()