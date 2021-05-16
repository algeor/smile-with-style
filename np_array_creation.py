import numpy as np

# 1. Loading the data set
wind_data = np.loadtxt('wind.data')
# Keeping only wind statistical data
all_wind_data = wind_data[:, 3:]

# Generating date labels
dates = []
for i in range(len(wind_data[:, 2])):
    dates.append(f'19{int(wind_data[ i, 0])}/{int(wind_data[ i, 1])}/{int(wind_data[ i, 2])}')
dates = np.array(dates).flatten()
# Inserting the date labels
all_data = np.column_stack((dates, wind_data))

# 2. All locations data (min, max, mean, std)
all_loc = []
all_loc.append(all_wind_data.min())
all_loc.append(all_wind_data.max())
all_loc.append(round(all_wind_data.mean(), 6))
all_loc.append(round(all_wind_data.std(), 6))
all_loc_array = np.array(all_loc)

# 3. Statistics over all days at each location
each_loc = []
each_loc.append(all_wind_data.min(axis=0))
each_loc.append(all_wind_data.max(axis=0))
each_loc.append(np.round(all_wind_data.mean(axis=0),6))
each_loc.append(np.round(all_wind_data.std(axis=0),6))
each_loc_array = np.array(each_loc)

# 4. Statistics over all locations for each day
each_day = []
each_day.append(all_wind_data.min(axis=1))
each_day.append(all_wind_data.max(axis=1))
each_day.append(np.round(all_wind_data.mean(axis=1), 6))
each_day.append(np.round(all_wind_data.std(axis=1), 6))
each_day_array = np.array(each_day)

# 5. Location of daily maximum
daily_max_loc = all_wind_data.argmax(axis=1)
daily_max_val_list = all_wind_data.max(axis=1)

# 6. Day of max reading
max_row, max_col = np.unravel_index(all_wind_data.argmax(), all_wind_data.shape)
max_date = dates[max_row]

# 7. Monthly means
monthly_list = []
for i in range(12):
    i += 1
    month_indice = wind_data[:, 1]==i
    month_data = all_wind_data[month_indice]
    month_means = np.round(month_data.mean(axis=0), 6)
    monthly_list.append(month_means)
monthly_means_array=np.array(monthly_list).reshape(12,12)
