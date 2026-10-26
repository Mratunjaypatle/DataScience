# numpy (Numerical Python) is a python library used to perform fast numerical calculation ..
import numpy as np 

numbers = [10,20,30]
print(numbers * 2)

marks = np.array([90,69,89,89]) # creating array
print(marks * 2)

#              
# a = np.arange(1, 10 , 2)
# print(a)

a = np.array([
    [10,20,30],
    [100,200,300]
])
print(a)
print(a.ndim)
print(a.shape)

# Mathematical Operation

x = np.array([10,20,30])
y = np.array([1,5,10])

print(x + y )
print(x - y )
print(x * y )
print(x / y )

# statical functions 

nums = np.array([70,80,90,60,100])

print(np.sum(nums))
print(np.mean(nums))
print(np.median(nums))
print(np.min(nums))
print(np.max(nums))
