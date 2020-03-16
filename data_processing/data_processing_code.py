'''Calculate n month diffrence transformation for a variable
For exmample, when conducting feature engineering for machine learning models, we
can use the code below to find the transformation for n month difference of a feature'''

#First Sorted by date to make sure when calculate the difference, date column is
#in a correct order
df.sort_values(by=['date'], inplace = True, acending = True)
# CC is a column that once you group by it, you get the date values for an aggeraion you want to use
diff_number = 3
df[new_name] = df.groupby(['CC'])[column_name].apply(lambda x:x.diff(diff_number))



'''Calculate n month rolling average transformation for a variable
For exmample, when conducting feature engineering for machine learning models, we
can use the code below to find the transformation for n month rolling average of a feature'''

df.sort_values(by=['date'], inplace = True, acending = True)
rolling_months = 6
df[new_name] = df.groupby(['CC'])[column_name].apply(lambda x:x.rolling(window=rolling_months).mean())