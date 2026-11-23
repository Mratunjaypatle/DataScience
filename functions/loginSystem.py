instagramUsername = input("Enter the username :")
instagramPassword = input("Enter the password :")


def userLogin (Username , Password) :
        if Username == instagramUsername and  Password == instagramPassword :
            return "User login successfull "
        else :
              return "User login unsucessfully"
instagram = userLogin("aman_09" , "aman@123")
print(instagram)





