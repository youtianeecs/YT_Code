import pandas as pd
import numpy as np
#%%
'''Calculate n month diffrence transformation for a variable
For exmample, when conducting feature engineering for machine learning models, we
can use the code below to find the transformation for n month difference of a feature'''

#First Sorted by date to make sure when calculate the difference, date column is
#in a correct order
df.sort_values(by=['date'], inplace = True, acending = True)
# CC is a column that once you group by it, you get the date values for an aggeraion you want to use
diff_number = 3
df[new_name] = df.groupby(['CC'])[column_name].apply(lambda x:x.diff(diff_number))

#%%
'''Calculate n month rolling average transformation for a variable
For exmample, when conducting feature engineering for machine learning models, we
can use the code below to find the transformation for n month rolling average of a feature'''

df.sort_values(by=['date'], inplace = True, acending = True)
rolling_months = 6
df[new_name] = df.groupby(['CC'])[column_name].apply(lambda x:x.rolling(window=rolling_months).mean())

#%%
# Forward Fill NA value for all NA, eg fill vallues between March and July if there are N/A in April, May
# and June. The forward fill processing may take a long time to finish
df.sort_values(by=['date'], inplace = True, acending = True)
# Group by CC and on the CC level, for each CC with different dates, forward fill them:
for cocc in df['CC'].unique():
    df[df['cc'] == cocc] = df[df['cc'] == cocc].ffill()

#%%
# Resample technique using bootstrap
# In machine learning 