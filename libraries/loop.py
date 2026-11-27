# Loop -> Loop is used to execute block of code multiple times until condition gets false 

# range(5) 0 1 2 3 4  
#       start  end 
# range(1,     5)  1 2 3 4 
# range(3 , 11) 3 , 4 ------ 8 , 9 , 10 
#     start  end     step 
# range(2 ,    11  ,   2)  2  4 6 8 10  

for i  in range(5) :
    print(i) 

print("*******************1 to 10**************")

for i in range(1 , 11) :
    print(i) # 1 , 2 , 3 , 10 


for i in range(2 , 21 , 2) :
    print(i)

#  print table of 7 

for i in range(7 , 71 , 7 ) :
    print(i)

for i in range(10) :
    print("hello world")