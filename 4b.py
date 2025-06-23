import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jane'],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'IT', 'Finance', 'HR', 'IT'],
    'Hours Worked': [40, 38, 45, 42, 37, 50, 48, 39, 44, 46]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

total_hours_by_dept = df.groupby('Department')['Hours Worked'].sum().reset_index()

print("\nTotal Hours Worked by Department:")
print(total_hours_by_dept)

pivot_table = df.pivot_table(values='Hours Worked', index='Department', aggfunc='sum')

print("\nPivot Table Summary (Total Hours by Department):")
print(pivot_table)

max_dept = total_hours_by_dept.loc[total_hours_by_dept['Hours Worked'].idxmax()]

print(f"\nDepartment with highest total working hours: {max_dept['Department']} with {max_dept['Hours Worked']} hours")
