import pandas as pd
import numpy as np

employees=pd.DataFrame({
    'employee_id':[1,2,3,4,5],
    'name':['John','Anna','Peter','Linda','Bob'],
    'department':['HR','IT','Finance','IT','HR']
})
salaries=pd.DataFrame({
    'employee_id':[1,2,3,6,7],
    'salary':[60000,75000,20000,45000,12000],
    'bonus':[5000,5000,4000,3000,2000]
})
print(employees)
print(salaries)

# merge
print(pd.merge(employees,salaries,on='employee_id',how='inner'))
print(pd.merge(employees,salaries,on='employee_id',how='outer'))
print(pd.merge(employees,salaries,on='employee_id',how='left'))
print(pd.merge(employees,salaries,on='employee_id',how='right'))

print(pd.concat([employees,salaries],axis=1))

# joining dataframes
# employees.join(salaries)
data = pd.DataFrame({
    "Category": ["Electronics","Clothing","Grocery","Electronics","Clothing","Grocery","Electronics"],
    
    "Store": ["Ahmedabad","Mumbai","Delhi","Pune","Ahmedabad","Mumbai","Delhi"],
    
    "Sales": [50000,20000,15000,60000,25000,18000,55000],
    
    "Quantity": [5,10,15,6,12,14,5],
    
    "Date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05","2024-01-06","2024-01-07"]
})
print(data)

sum_category=data.groupby('Category')['Sales'].sum()
print(sum_category)

sum_store=data.groupby('Store')['Sales'].sum()
print(sum_store)

sum_category_store=data.groupby(['Store','Category'])["Sales"].sum()
print(sum_category_store)

# Aggregation Functions
mean=data["Sales"].mean()
print(mean)

agg=data["Sales"].agg(["sum","min","max","mean","median","count","std","var"])
print(agg)

# Data Operations
df1=pd.DataFrame({
    'A':[1,2,3,4,5],
    'B':[10,20,30,40,50],
    'C':[100,200,300,400,500]
})
print(df1)
print(df1.shape)
print(df1.columns)
print(df1.info())
print(df1.describe())
print(df1['A']+10)
print(df1['B']**2)

# OR

def square(x):
    return x**2
df1['B']=df1['B'].apply(square)
df1['D']=df1['B'].apply(square)
print(df1)