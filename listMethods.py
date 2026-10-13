'''
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort(

marks = [87,78,90,98,67,98]
mark.sort()
)	Sorts the list
'''

number = [10,20,30]
number.append(50)
number.clear()
print(number)

fruits = ["mango" , "apple"]
#            0          1        2 
fruits.extend( ["banana" , "grapes"] )
# ['mango', 'apple', 'banana', 'grapes']
#    0         1        2         3  

print(fruits[3])
     #        index  , element 
fruits.insert(2 , "Pineapple")
print(fruits)

# fruits.remove("apple")
fruits.pop() # -> removes elemets end of the list 
print(fruits)   

fruits.remove("apple")
print(fruits)
print(fruits.index("Pineapple"))
fruits.reverse()
print(fruits)


marks = [87,78,90,98,67,98]
marks.sort()
print(marks)