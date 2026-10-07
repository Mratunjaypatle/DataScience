# Python Data types .. 

# 1. int  -> Integers / Numbers 
# 2. str -> String / Text / Sentence 
# 3. float -> Decimal Numbers  (2.4)
# 4. bool -> True and False
# 5. list -> Ordered collection or mutable collection 
# 6. set -> Unordered collection of unique element..
# 7. tuple -> Ordered and immutable collection 
# 8. dict -> Collection of key - value pairs 
# 9. complex
# Python variable

# variable is used to store the value 

a = 100 + 100 # 200 
name = 'Arun kumar' 
age = 25   
b = 20.3
isOct = True 
isNov = False 

# print(a + 100)

print("Name is " , name , "and age is " , age )
print(type(a))
print(type(name))
print(type(b))
print(type(isOct))

# print(b)

# way to define a variable 

age_of_sumit = 20 

number = 4 + 5j
print(number)
print(type(number))


student1 = "aman"
student2 = "rahul"
student3 = "priya"

print(student1)

print(student2)

print(student3)

# list is Ordered collection and mutable collection 
# indexing  starts from 0
# Mutable means which can be changed ...


students = ["aman" , "rahul" , "priya"]
# indexing    0         1         2 
students[0] = "Aditya"

print(students)
print(students[0])
print(students[2])

print(type(students))

#set is unordered and immutable
# set does not provide the indexing 
cities = {"delhi" , "mumbai" , "hyderabad"}
print(type(cities))

# tuple -> tuple is an ordered and immutable collection
# tuple contains indexing  -> True 

cordinate = (10,20)
#             0  1
print(cordinate)
print(type(cordinate))
print(cordinate[0])


studentData = {
#       key  :  value 
      "name" : "Jai" ,
       "age" : 23 ,
       "city" : "Mumbai"
}
print(studentData)
print(studentData["name"])
print(studentData["age"])
# In disc we get the data using key..









