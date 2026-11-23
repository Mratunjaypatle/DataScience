# logical operators and or 
# login system

#databse data 
dbUsername = "sumit_08"
dbPassword = "sumit@123"

username = "sumit_08"
password = "sumit@123"

if username == dbUsername and password == dbPassword :
    print("user login successfully")
else :
    print("user login unsucessfully")

# if a student gets more than 33 marks then he will pass , if students gets more than 90 than he is marrit list

marks = 98

if marks > 90 and marks > 33 :
    print("pass and marrit list") 
else :
    print("fail")


# OR gate

# if a user have 60k ruppes or special card they he can purchase laptop 

user_amount = 10000
user_special_card = False

if user_amount >= 60000 or user_special_card == True :
    print("he can purchase laptop")
else :
    print("he can not purchase laptop")


    