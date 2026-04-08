# Pandas refer to reading document before implementing it 
# Pandas used for data cleaning, data analysis, data transformation, data visualization, data aggregation, file handling, data filtering & selection and time series analysis 
# A Series is a 1D labeled array capable of holding any dataype.The axis labels are collectively called the index.Series are vertical in nature.

import numpy as np
import pandas as pd

labels=['a','b','c']
my_list=[10,20,30]
my_arr=np.array([10,20,30])
d={'a':10,'b':20,'c':30}

print("\nLabels Datapoints")
# Sending list as series with default index
print(pd.Series(my_list))

# Sending list as series with defined index
print(pd.Series(my_list,index=labels))

# Sending array as series with default index
print(pd.Series(my_arr))

# Sending dictionary as Series
print(pd.Series(d))

# Collection of multiple series form a dataframe 

# Passing list as dataframe
data_list=[
    ["Khushi",21,"Vadodara",65000],
    ["Muskan",23,"Mathura",50000],
    ["Swara",20,"Pune",70000],
    ["Pranita",18,"Mumbai",45000],
    ]
print(pd.DataFrame(data_list))
print(pd.DataFrame(data_list,columns=["Name","Age","City","Salary"]))

# Passing dict as collection i.e. dataframe
data={
    "Name": ["Khushi","Muskan","Swara","Pranita"],
    "Age": [21,23,20,18],
    "City": ["Vadodara","Mathura","Pune","Mumbai"],
    "Salary": [65000,50000,70000,45000],
    }
x=pd.DataFrame(data)
print(x[["Name","City"]])

# add a column in our collection
data["Designation"]=["Team Lead","HR","Doctor","CEO"]
print(pd.DataFrame(data))

# removing a column from our collection : drop for remvoing temporarily and not directly in df : inplace for removing it competely 
x.drop("Name",axis=1,inplace=True)
print(x)

# Selecting row
print(x.loc[0])
print(x.iloc[3])




