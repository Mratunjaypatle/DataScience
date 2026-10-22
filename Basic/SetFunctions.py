s = {1 , 2 , 3}
print(s)

# functions / methods in the sets

# .add() is used to add element in a set

s.add(4)
print(s)

#update() is used to add multiple values from another iterable 

set1 = {1,2}

set1.update([3 , 4 , 5]) 

# discard removes an element if present , it does not raise an erorr if the element is missing ..

set1.remove(2)
set1.discard(3)
print(set1)


set2 = {10 , 20 , 30}
print(set2)

#pop removes and returns the element 
x = set2.pop()
print(set2)
print(x)

# clear -> removes all elements 
set2.clear()
print(set2)