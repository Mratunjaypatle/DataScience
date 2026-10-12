# methods -> In python , string methods are built in function used to manipulate string .. 

text = "Hello"
print(text)
print(text.upper()) # Converts into uppercase
print(text.lower()) # Converts into lowercase

newText = "data science with python"

print(newText.title()) # it converts every fisrt character of word into uppercase
print(newText.capitalize()) # it converts only fisrt character of first word into uppercase

myString = "    Hello"
print(myString)
print(myString.strip())

print("-----------------------------------")


# input user 

# input () -> >used to take input from the user 

'''
username = input("Enter the username : ")
password = input("Enter the password : ")

if username == "satyam_mehta" and password.strip() == "satyam@123" :
    print("user login successfully") 
else :
    print("user login unsuccessfully")
   '''

print(newText.replace("python" , "R programming"))   

print(len(myString))
    
myword = "          hyeeeee      charan      "

print(myword.strip())

# There are some string methods which returns string then some methods return numeric value then some methods return the boolean value ..

print(newText.startswith("python"))
print(newText.endswith("python"))


