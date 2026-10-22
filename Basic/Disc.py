students = {
    "name" : "Naman" ,
    "age" : 21 , 
    "marks" : 80
}

print(students["age"])
print(students.get("city"))

# functions in the disc 

print(students.keys())
print(students.values())
print(students.items())

# update -> we can add new key and values 

students.update( {
        "city" : "Kolkata"
}  )

print(students)

newStudent = students.copy()
print(newStudent.clear())
