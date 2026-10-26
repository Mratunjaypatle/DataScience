import pandas as pd 

employee = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Aman sharma", "Jitendra", "Amith", "Charan", " Himanshu"],
    "department": ["Engineering", "Marketing", "Finance", "Human Resources", "Engineering"],
    "salary": [85000, 32000, 78000, 60000, 92000],
    "experience": [4, 2, 5, 3, 7]
})
print(employee)

# find employee earning more than 45000

result = employee[employee["salary"] > 45000]
print(result)

# find employee who is from Marketing department

result2 = employee[employee["department"] == "Marketing"]
print(result2)