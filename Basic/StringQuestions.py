# Questions for string methods

# check the username 
# vikas123 -> invalid  , vikas -> valid 

username = input("Enter the username ")
if username.isalpha() :
    print("valid username")
else :
    print("invalid username")

# check the password length 

# password limit is -> 8 , 1234 -> invalid 

password = input("Enter the username ")

if len(password) >= 8 :
    print("valid password")
    print(len(password))
else :
    print("invalid password")
    
#Remove extra spaces from the name 

name = input("Enter your name")
name = name.strip()

print(name)


# check file extension ..
# .pdf , .jpg , .py , .html , .js

# identify is the file is pdf format..?

filename = input("Enter the fileName  ")
print(filename)

if filename.endswith(".pdf") :
    print("This is PDF file")
else :
    print("This is other file")


# find a word in the sentence 

sentence = input("enter your sentence")
findWord = "python"

if findWord in sentence :
    print(findWord , "Found")
else :
    print(findWord , " not found")
 
 
 