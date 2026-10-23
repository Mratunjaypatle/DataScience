# functions perform specific tasks. you can use it whenever we need it .. without writing the same code again and again , to divide large task to small task
 
# def function_name() :
    # code to execute 
    # calling the function

def greet() :
    print("good evening")

def sayHello() :
    print("hello everyone")

# greet()
# greet()
# greet()


# two types of functions in the python

# pre defined functions , user defined functions

# parameter and argument in the function .. 


def sayName (name) : # parameter
    print("hello " , name )

sayName("Priya") # argument
sayName("Rohan")
sayName("Hansika")
sayName("Manvitha")

def sum (a , b) :
    print(a+b)

sum(10,20)
sum(100,200)


# employee details 

def emp (id , name , age , salary , city) :
    print(id , name , age , salary , city)

emp(101 , "anjali" , 27 , 56000 , "Chennai")
emp(102 , "bittu" , 25 , 1200000 , "Indore")


# Functions with return statement 

def multiply (a,b) :
    return a*b 

result = multiply(10,5)

print(result)   


def sayThanks (name = "Priya") :
    print("Thanks to" , name)

sayThanks()
sayThanks("Aman")