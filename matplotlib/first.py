# Matplotlib is a comprehensive, open-source Python library used for creating static, animated, and interactive data visualizations

# Matplotlib can create 
'''
Line chart , Bar chart , Histogram , Pie charts  ,Scatter Plot , Box plot
'''

import matplotlib.pyplot as plt

tests = [1 , 2  , 3 , 4  , 5]
marks = [45 , 55 , 60 , 75 , 90]

plt.plot(tests , marks , marker="o" )
plt.title("Student Performance")
plt.xlabel("Test Numbers")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# plt.title -> Adds a chart title
# plt.xlabel() -> labels the x axis , plt.ylabel ->  labels the y axis
# plt.grid(true) -> displays grid line 


from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

days = ["monday" , "tuesday" , "wednesday" ,"thursday" , "friday" , "saturday" , "sunday"]
temperature = [23, 24 , 23 , 23.5 , 24.5 , 22 , 25]

plt.plot(days , temperature , marker = "o")
plt.title("Weekly weather details")
plt.xlabel("Days of the week")
plt.ylabel("Temperature (°c)")
plt.grid(True , linestyle='--')

plt.show()


# Bar chart -> A bar chart is a data visualization that presents categorical data using rectangular bars
