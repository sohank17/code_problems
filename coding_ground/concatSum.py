#Problem Statement: You are given an array of numbers. You need to concatenate them in different patterns and return the sum of these patterns. (Example: Array=[1,10], 
#                   Sum = 110,101,11,1010 = 1232)

a=[1,10] 
import numpy as np

def concat(a):
    sum_=0
    a = list(map(str,a))
    a = np.array(a)
    b=len(a)
    for i in a:
        array_copy= np.array([i]*b)
        added_array = np.char.add(a, array_copy).astype(np.int64)
        sum_ += np.sum(added_array)
    return sum_
    
print(concat(a))
