import pandas as pd
import matplotlib.pyplot as plt
from np_array_creation import *

# Color schemas
color4 =  ['#d5f7c7', '#75e547', '#3fa017', '#245c0d']
color12 = ['#d5f7c7', '#bcf2a5', '#95eb71', '#75e547', '#4ec61c', '#47b41a',
           '#3fa017', '#388e14', '#307b12', '#2d7210', '#245c0d', '#1e4d0b']
# Data frame for all data
locations_names=['Loc1','Loc2', 'Loc3', 'Loc4', 'Loc5', 'Loc6' , 'Loc7',
                 'Loc8', 'Loc9', 'Loc10', 'Loc11', 'Loc12']
months_names = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
df = pd.DataFrame(all_wind_data,index=dates,  columns =locations_names)


# 2. Generalized data series for min, max, mean and std
all_loc_series = pd.Series(all_loc_array, index = ['Min', 'Max', 'Mean', 'STD'])
all_loc_series.plot.bar(color=color4)

# 3. Data Frame for statistical data over all days at each location')
each_loc_df = pd.DataFrame(each_loc, index= ['Min', 'Max', 'Mean', 'STD'],  columns =['Loc1','Loc2', 'Loc3', 'Loc4', 'Loc5', 'Loc6' , 'Loc7', 'Loc8', 'Loc9', 'Loc10', 'Loc11', 'Loc12'])
each_loc_df.plot.bar(color=color12)


# 4. Data frame for statistical data over all locations for each day
each_day_df = pd.DataFrame(each_day_array, index=['Min', 'Max', 'Mean', 'STD'], columns=dates)

# 5. Data frame for location of daily maximum')
# Location column will be converted to location name and a date will be added as per row
daily_max_loc_list = []
daily_max_days_list = []
counter = 0
for i in daily_max_loc:
    daily_max_loc_list.append(locations_names[i])
    daily_max_days_list.append(dates[counter])
    counter+=1
# Zipping pairs into tuples in or to display in a data frame
data_tuples = list(zip(daily_max_loc_list,daily_max_val_list))
daily_max_loc_df = pd.DataFrame(data_tuples, index=daily_max_days_list, columns=['Location','Max value'])

# 6. Data frame for a day of max reading - not needed


# 7. Data frame for monthly mean per locations
monthly_means_df = pd.DataFrame(monthly_means_array, index=months_names, columns=locations_names)

