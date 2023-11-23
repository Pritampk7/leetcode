import sys
import time

import pandas as pd

# Specify the file path and sheet name
file_path = 'WorkItem.xlsx'
sheet_name = 'WorkItemSearchResult'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)


# Specify the column you want to filter (replace 'X' with your actual column name)
column_name = 'Date'

# Specify the value you want to filter for (replace 'bath' with your actual value)
desired_value = 'Batch'

# Filter rows based on the condition
filtered_df = df[column_name] == desired_value

# Display the resulting DataFrame
print(filtered_df)

import pandas as pd
import numpy as np
file_loc = file_path
df = pd.read_excel(file_loc, index_col=None, na_values=['Batch'], usecols="Y:Y")
print(df)