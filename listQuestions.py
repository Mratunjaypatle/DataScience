# Questions for List methods

# Add an element in the list

fruits  = ["Mango" , "Apple"]

fruits.append("Orange")
print(fruits)

if "orange" in fruits :
    print("Orange added")
else :
    print("Orange not added")
 
numbers = [10,20,30]

if 30 in numbers :
    print("30 is found")
    
colors = ["Red" , "Blue" , "Green" , "Blue"]

colors.remove("Blue")
colors.remove("Blue")
if "Blue" in colors :
    print("Blue is still present")
else :
    print("Blue is completely removed")
    
 # check is list sorted or not
  
marks = [89,45,67,43,90]

marks.sort()
# [43, 45, 67, 89, 90]
#   0   1   2   3   4
print(marks)

if marks[0] < marks[1] :
    print("sorted list")
else :
    print("unsorted list")

elements = [1 , 2, 4, 5, 2, 6, 2]
count = elements.count(2)
print(count )

if count > 2 :
   print("Duplicate")


