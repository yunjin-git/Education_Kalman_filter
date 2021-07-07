# This code is based on '칼만 필터는 어렵지 않아,김성필"
# code developer : yunjin Kyung, MyoungJi univerity
import numpy as np

def Avgfilter (data):
    n=1
    num_of_data = data.shape[0]
    avg = np.zeros(num_of_data)# Return average data Array init
    while n <= num_of_data:
        avg[n-1]=(n-1)/(n)*avg[n-2]+(1/n)*(data[n-1])
        n=n+1

    return avg
   
    
