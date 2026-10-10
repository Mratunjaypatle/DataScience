# Positive negative number

num = 0 

if num > 0 : 
    print(num ,  "is positive number")
elif num == 0 :
    print("Number is Zero")
else : 
    print(num , "is negative number")
    
# Error -> Syntax error , logical error 

# problem -> even number and odd number 

# 10 % 2 -> 0 

number = 13 

if number % 2 == 0 :
    print("Even number")
else :
    print("Odd number")
    
# and -> The and operator return True only when both conditions are True 
username = "satyam_mehta"
password = "satyam@1234"

if username == "satyam_mehta" and password == "satyam@123" :
    print("user login successfully") 
else :
    print("user login unsuccessfully")


a = 100
b = 20 
c = 200
print("--------------and gate-----------------")
if a>b and a>c :
   print("a is greater")
else :
    print("a is not greater")
    
    
 # OR -> The or operator return True only when one conditions is True 
 
 
print("--------------or gate-----------------")
 
if a>b or a>c :
   print("a is greater")
else :
    print("a is not greater")
 

# If either aman has 1000 ruppes or he has entry pass -> aman can enter.      
  
aman_amount = 500
aman_card = True 

if aman_amount >= 1000 or aman_card :
    print("he can enter in the concert")
else : 
    print("he can not enter in the concert")
      
      
# Student admission problem for college-> Student age should be greater than and equals to 18 and student percentage should be more than and equals to 65% 

Student_age = 19
Student_percentage = 63

if Student_age >= 18 and Student_percentage >= 65 :
    print("student can take admission")
else :
    print("student can not take admission")
   
  