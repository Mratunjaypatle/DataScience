import math 
# print the square root of 25 
print(math.sqrt(25))
print(math.pow(2 , 3))
print(math.factorial(5))

# 1 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2 
# ceil -> 2
# floor -> 1
print(math.floor(1.5))
print(math.ceil(1.1))

# Loop -> Loop is used to execute block of code multiple times until condition gets false 

# range(5) 0 1 2 3 4  
#       start  end 
# range(1,     5)  1 2 3 4 
# range(3 , 11) 3 , 4 ------ 8 , 9 , 10 
#     start  end     step 
# range(2 ,    11  ,   2)  2  4 6 8 10  

for i  in range(5) :
    print(i) 