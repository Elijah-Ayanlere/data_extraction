import pandas as pd
import numpy as np

# Step 1: Read the CSV file and extract the PRCP column
df = pd.read_csv('C:\\Datasets\\BicycleWeather.csv')
df.head()
print(df)
prcp_column = df['PRCP']

# Convert the PRCP column to a NumPy array
prcp_array = prcp_column.to_numpy()

# Step 2: Separate numbers from NaN (missing values)
numbers_only = prcp_array[~np.isnan(prcp_array)]

# Step 3: Separate zeros and non-zeros using boolean masking
zeros = numbers_only[numbers_only == 0]
non_zeros = numbers_only[numbers_only != 0]

# Step 4: Multiply every value in the non_zeros array by 100 and divide by 250
non_zeros_modified = non_zeros * 100 / 250

# Step 5: Calculate the required statistics
# a. Median precip on rainy days (considering all non-NaN values)
median_precip_rainy_days = np.median(numbers_only)

# b. Median precip on non-zero days
median_precip_non_zero_days = np.median(non_zeros)

# c. Maximum precip on all days
max_precip_all_days = np.max(prcp_array)

# d. Median precip on non-zero rainy days
non_zero_rainy_days = prcp_array[(~np.isnan(prcp_array)) & (prcp_array > 0)]
median_precip_non_zero_rainy_days = np.median(non_zero_rainy_days)

# Print the results
print("Median precip on rainy days:", median_precip_rainy_days)
print("Median precip on non-zero days:", median_precip_non_zero_days)
print("Maximum precip on all days:", max_precip_all_days)
print("Median precip on non-zero rainy days:", median_precip_non_zero_rainy_days)