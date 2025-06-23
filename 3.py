import numpy as np
# 1. Create 1D and 2D arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
# 2. Perform operations
# Addition
add_result = array_1d + 10
print("\nAddition with 10:", add_result)
# Multiplication
mult_result = array_2d * 2
print("Multiplication by 2:\n", mult_result)
# Slicing
sliced_1d = array_1d[1:4]
print("Sliced 1D Array [1:4]:", sliced_1d)
# Reshaping
reshaped = np.reshape(array_1d, (5, 1))
print("Reshaped 1D to 2D:\n", reshaped)
import pandas as pd
# Create DataFrames
students = pd.DataFrame({
'ID': [1, 2, 3, 4],

'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [24, 27, 22, 32],
'Marks': [85, 62, 90, 70]
})
grades = pd.DataFrame({
'ID': [1, 2, 3, 4],
'Grade': ['A', 'C', 'A+', 'B']
})
# Merging DataFrames
merged_df = pd.merge(students, grades, on='ID')
print("\nMerged DataFrame:\n", merged_df)
# Add derived column
merged_df['Passed'] = merged_df['Marks'] >= 60
print("\nAdded 'Passed' column:\n", merged_df)
# Filtering
print("\nStudents who scored above 80:\n", merged_df[merged_df['Marks'] >
80])
# Grouping
grouped = merged_df.groupby('Grade')['Marks'].mean()
print("\nAverage marks per grade:\n", grouped)
# Sorting
sorted_df = merged_df.sort_values(by='Marks', ascending=False)
print("\nSorted by Marks (descending):\n", sorted_df)
# Handling missing data
merged_df.loc[4] = [5, 'Eve', 29, None, 'B+', True]
print("\nDataFrame with Missing Values:\n", merged_df)
# Fill and drop
print("\nFill missing Marks with 0:\n", merged_df['Marks'].fillna(0))
import matplotlib.pyplot as plt
names = merged_df['Name']

marks = merged_df['Marks'].fillna(0)
age = merged_df['Age']
# Line Plot
plt.figure()
plt.plot(names, marks, marker='o', color='blue')
plt.title("Line Plot: Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
# Bar Plot
plt.figure()
plt.bar(names, age, color='green')
plt.title("Bar Plot: Student Age")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()
# Pie Chart
plt.figure()
plt.pie(marks, labels=names, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart: Marks Distribution")
plt.axis('equal')
plt.show()
# Scatter Plot
plt.figure()
plt.scatter(age, marks, color='purple')
plt.title("Scatter Plot: Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
# Histogram
plt.figure()
plt.hist(marks, bins=5, color='orange', edgecolor='black')
plt.title("Histogram: Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
# Box Plot

plt.figure()
plt.boxplot(marks, patch_artist=True)
plt.title("Box Plot: Marks Distribution")
plt.ylabel("Marks")
plt.show()



























print("\nDrop rows with any missing values:\n", merged_df.dropna())
