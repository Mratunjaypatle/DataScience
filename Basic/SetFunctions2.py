a = {1,2,3,4,5}
b = {4,5,6,7}

# union() returns the unique elements from both side 

print(a.union(b))

# intersection return only common elements from the bith sides

print(a.intersection(b))

# difference() return elements in a that are not in b

print(a.difference(b))


# length of the set
print(len(a))

print(3 in a)
print(b.issubset(a))
print(b.issuperset(a))
