import pandas as pd

# File paths
file_path_tesla = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\TESLA Search Trend vs Price.csv'
file_path_btc_search = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Bitcoin Search Trend.csv'
file_path_btc_price = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Daily Bitcoin Price.csv'
file_path_unemployment_2004_2020 = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\UE Benefits Search vs UE Rate 2004-20.csv'

# Load the data into DataFrames
df_tesla = pd.read_csv(file_path_tesla)
df_btc_search = pd.read_csv(file_path_btc_search)
df_btc_price = pd.read_csv(file_path_btc_price)
df_unemployment_2004_2020 = pd.read_csv(file_path_unemployment_2004_2020)

# Function to convert string columns to datetime
def convert_to_datetime(df, date_column):
    if df[date_column].dtype == 'object':
        df[date_column] = pd.to_datetime(df[date_column])
        print(f"{date_column} column in DataFrame converted to datetime.")
    else:
        print(f"{date_column} column in DataFrame is already in datetime format.")
    return df

# Convert 'MONTH' or 'DATE' columns to datetime for all DataFrames
df_tesla = convert_to_datetime(df_tesla, 'MONTH')
df_btc_search = convert_to_datetime(df_btc_search, 'MONTH')
df_btc_price = convert_to_datetime(df_btc_price, 'DATE')
df_unemployment_2004_2020 = convert_to_datetime(df_unemployment_2004_2020, 'MONTH')

# Double-check the data types
print("\nData types after conversion:")
print("Tesla DataFrame:")
print(df_tesla.dtypes)
print("\nBitcoin Search DataFrame:")
print(df_btc_search.dtypes)
print("\nBitcoin Price DataFrame:")
print(df_btc_price.dtypes)
print("\nUnemployment 2004-2020 DataFrame:")
print(df_unemployment_2004_2020.dtypes)
