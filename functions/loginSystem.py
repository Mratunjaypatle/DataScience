Username = input("Enter the username :")
Password = input("Enter the password :")


def userLogin (username , password) :
        if username == Username and  password == Password :
            return "login successfull "
        else :
              return "login unsucessfully"
        
# instagram = userLogin("aman_09" , "aman@123")
# print("Instagram user " + instagram)

facebook = userLogin("ashish_123" , "ashish@123")
print("Facebook user " + facebook)










