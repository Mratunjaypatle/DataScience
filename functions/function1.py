# function 

# define a function -> def
# formate -> use ()
# how to call -> 

def greet() :
    print("good morning")

greet() # -> calling of the function

def login () :
    print("login successfully")

login()

# parameter in the function 

def sum (a , b) :
    print(a + b)

sum(10 , 20)
sum(100 , 200)

 
def sayName (name) :
    print("My name is " , name)

sayName("Nikhil")
sayName("rohit")


def isLogin (name , password) :
    if name == "Rohit" and password == "123123" :
        return True
    else :
        return False

loginDetails = isLogin("mohit" , "123123")

if loginDetails :
    print("login successfully")
else :
    print("login unsuccessfully")