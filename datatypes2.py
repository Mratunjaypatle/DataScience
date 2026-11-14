# A set in Python is an unordered, mutable collection of unique and hashable elements, implemented internally using a hash table for efficient operations.  Unlike lists or tuples, sets do not allow duplicates and do not support indexing or slicing, though you can iterate through them. 
# mutable -> we can not perform any changes .. 

marks = {10 , 20 , 30 }
print(marks)
print(type(marks))


# A Python dictionary is a mutable, insertion-ordered collection of key-value pairs where keys must be unique and immutable (e.g., strings, numbers, list m sets , tuples). 

user1 = {
#     key  : value     
    "Name" : "Abhay" ,
    "Age" : 23 , 
    "City" : "Hyderabad",
    "score" : [9,8,5,6,9,10] ,
    "Set" : {10,20}
}

print(user1)
print(user1["Name"])
print(user1["Age"])
print(user1["City"])
print(user1["score"][0])
print(user1["Set"])


 
