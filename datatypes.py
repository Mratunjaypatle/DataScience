'''
list , tuple , set , dictionary
'''
# 
# A Python list is a mutable, ordered, and dynamic collection used to store multiple items in a single variable
# Lists are defined using square brackets []
# List contains indexing .. 
# indexing starts from 0
# mutable -> changes are allowed

students = ["abhay" , "himanshu" ,  "charan" , "anamika" , 12 , 34 , True]
#              0          1             2           3

students[0] = "amit"

print(students[0])
print(students[1])
print(students[3])
print(students)


# tuple

# In Python, a tuple is an ordered, immutable collection of elements, used to store multiple items in a single variable.  Unlike lists, which are mutable and defined with square brackets [], tuples are defined using parentheses () and cannot be modified, added to, or removed from after creation

cities = ("Delhi" , "Mumbai" , "kolkata")

print(cities)
print(cities[0])