import numpy as np
import pandas as pd

# Load your csv file
df=pd.read_csv('path to csv file')

# Shows top 5 rwos of your csv file
df.head()

# Feature Extraction
# here location shows row index
# and title shows uss row index ka particular column
df.loc[2]['Title']

# task to extract title mese episodes ka count
def extract_episodes(txt):
    check=False
    data=""
    for i in txt:
        if i==')':
            check=False
            break
        if i=='(':
            check=True
        if check==True:
            data+=i
    return data

# applying function to title column and creating a new column for it as episodes
df['Episodes']=df['Title'].apply(extract_episodes)

# replacing ' eps' with '' and saving it to episodes
df['Episodes']=df['Episodes'].str.replace(" eps","")

# converting datatype of episodes to int from str
df['Episodes']=df['Episodes'].astype(int)

# now we want to extract time stamp from title and save it in another column (Apr 2009 - Jul 2018)
def extraction_time(txt):
     check=False
     data=''
     for i in range(len(txt)):
         if txt[i]==")":
            for j in range(i+1,i+20):
                 data+=j
            return data
         
df['Totla-Time']=df['Title'].apply('extraction_time')

# Which anime has highest score
df[df["Score"]]=df['Score'].max()['Title']

# top 5 highest scoring anime
df['Score'].value_counts
df['Score'].unique
df['Score'].head
df['Title'].head

# whenever recieve new data use these few fun on data 
df=pd.read_csv("path")
df.shape
df.info
df.describe