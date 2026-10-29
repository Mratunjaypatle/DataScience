# Pandas is a python library that is used to data manipulation and analysis. 
# pip install pandas
'''
 There are two main Data Structure of pandas
 Series , DataFrame
 A Pandas Series is a one-dimensional labeled array capable of holding any data type, analogous to a single column or a Python list with an index. 
   A Pandas DataFrame is a two-dimensional labeled data structure with columns of potentially different types, functioning like a spreadsheet or SQL table composed of multiple Series objects. 
'''
import pandas as pd 
print(pd.__version__)

marks = pd.Series([10,20,30,40])
print(marks)

students = pd.Series(["Anuj" , "Bhumika" , "Chrish"])
print(students)

data = {
    "Name":   ["Aman", "Rahul", "Priya", None, "Vikram",
               "Ankit", "Pooja", None ,  "Kavya", "Arjun",
               "Neha", "Suresh", "Divya", "Karan", "Meera"],
    "age":    [None, None, 25, 22, 28,
               26, 21, None, None, 27,
               23, 35, 29, 25, None],
    "city":   ["Raipur", "Kochi", "Chennai", "Delhi", "Mumbai",
               "Pune", "Jaipur", "Bengaluru", None, "Kolkata",
               "Ahmedabad", "Surat", "Indore",None , "Lucknow"],
    "salary": [35000, 42000, None, 30000, 55000,
               40000, 28000, None, 38000, 50000,
               32000, 70000, 45000, 36000, 29000],
    "gender": ["M", "M", "F", "F", "M",
               "M", "F", "M", "F", "M",
               "F", "M", "F", "M", "F"]
}
df = pd.DataFrame(data)
print(df)

# there are multiple function in pandas 

# head -> head() displays the first five rows by default
print(df.head(3))
print("*******************************************")
# tail() -> it helps to display last five rows by default

print(df.tail(2))

# shape -> shape is an attribute not a method , we do not use paranthese() , it provides number of columns & rows..

print(df.shape)

print(df.columns.tolist())

# print(df.info())
missingValues = df.isnull().sum().sum()
print(f"There are {missingValues} missing values in the data")

