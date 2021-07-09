# This code is based on '칼만 필터는 어렵지 않아,김성필"
# code developer : yunjin Kyung, MyoungJi univerity
import numpy as np

def get_static_sample(static_data,noise_val):
    sample = static_data + np.random.normal(0,noise_val)
    return sample

def get_linear_sample(slope,inc,noise_val):
    sample = slope*inc + np.random.normal(0,noise_val)
    return sample

def get_dynamic_sample():
    return 0
    
def Avgfilter4Array (data):
    n=1
    num_of_data = data.shape[0]
    avg = np.zeros(num_of_data)# Return Array init
    while n <= num_of_data:
        avg[n-1]=(n-1)/(n)*avg[n-2]+(1/n)*(data[n-1])
        n=n+1
    return avg

def Avgfilter(k,meas_x,pre_avg):
    a = (k-1)/k
    avg = a*pre_avg+(1-a)*meas_x  # Return Array init
    return avg

def MovAvgfilter (data,k) :
    n=1
    num_of_data = data.shape[0]
    result = np.zeros(num_of_data)# Return Array init
    while n < num_of_data :
        result[n] = result[n-1]+(data[n]-data[n-k])/k
        n=n+1

    return result