import numpy as np
import pandas as pd

data={
    "Name": ["Khushi","Muskan","Swara","Pranita"],
    "Age": [21,23,20,18],
    "City": ["Vadodara","Mathura","Pune","Mumbai"],
    "Salary": [65000,50000,70000,45000],
    }

x=pd.DataFrame(data)
print(x)

# Selection
print(x.loc[[0,1]][["City","Salary"]])
print(x.loc[[2,3]][["Name","Age"]])

# Conditional selection
z=x[x["Age"]>20]
print(z)
y=x[(x["Age"]>20) & (x["City"]=="Vadodara")]  # Age is greater than 20
print(y)


# Finding Missing data
data_nan={
    "Name": ["Khushi","Muskan",np.nan,"Pranita"],
    "Age": [21,23,20,np.nan],
    "City": ["Vadodara","Mathura","Pune","Mumbai"],
    "Salary": [65000,np.nan,70000,45000],
    }

df_nan=pd.DataFrame(data_nan)
print(df_nan)

# Finding missing data
print("Dataframe missing values")
print(df_nan.isna().sum())
print(df_nan.isna().any())

# Removing missing values
print(df_nan.dropna())
# thresh gives atleast 3 null values must be there
print(df_nan.dropna(thresh=3))

# fill missing values with zero
print(df_nan.fillna(0))

# filling missing values with mean value
# print(df_nan.fillna(df_nan.mean()))

