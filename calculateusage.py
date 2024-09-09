import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('1.csv')
df['created_at']= pd.to_datetime(df['created_at'])
df = df.dropna(subset = ['field1']) # drop rows with NaN in field1 
print(df)
tempvar = False
total_time = 0
for index, row in df.iterrows():
    #print(row['field1'])
    if row['field1'] == 1 and tempvar == False:
        start= row['created_at']
        tempvar = True        
    if row['field1'] == 0 and tempvar == True:
        end = row['created_at']
       
        time_elapsed = row['created_at'] - start
        time_elapsed_in_minutes = time_elapsed.total_seconds() / 60 

        tempvar = False
        total_time = total_time + time_elapsed_in_minutes


#print(df['created_at'].values[1])
#print(df['created_at'].values[-1])

#print(round(total_time))

print ("Between ", df['created_at'].values[1], " and ", df['created_at'].values[-1], "motion was detected in mikes office for ", round(total_time), " minutes")

unique_dates = df['created_at'].dt.date.unique()
print("Unique dates:", unique_dates)
for date in unique_dates:
    date_df = df[df['created_at'].dt.date == date]
    tempvar = False
    total_time = 0
    for index, row in date_df.iterrows():
        #print(row['field1'])
        if row['field1'] == 1 and tempvar == False:
            start= row['created_at']
            tempvar = True        
        if row['field1'] == 0 and tempvar == True:
            end = row['created_at']
        
            time_elapsed = row['created_at'] - start
            time_elapsed_in_minutes = time_elapsed.total_seconds() / 60 

            tempvar = False
            total_time = total_time + time_elapsed_in_minutes

    print("Motion was detected in mikes office on", date, "for", round(total_time), "minutes")
