import pandas as pd
import matplotlib.pyplot as plt
from evds import evdsAPI

# Define a function to read the API key from the specified file path.
def read_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

# Read the API key from the 'tcmb_evds_api_key.txt' file.
api_key = read_api_key("tcmb_evds_api_key.txt")

# Create an EVDSAPI object with the EVDS API key.
evds = evdsAPI(api_key)

# Request Dollar/TRY exchange rate data for a specific date range.
# 'TP.DK.USD.A.YTL' code represents the Dollar/TRY exchange rate data from TCMB.
# We define the date range using the 'startdate' and 'enddate' parameters.
usd_try_df = evds.get_data(['TP.DK.USD.A.YTL'], startdate="30-12-2020", enddate="30-06-2023")

# Fill missing values in the DataFrame using forward fill method.
usd_try_df = usd_try_df.fillna(method='ffill')

# Update column names of the DataFrame.
usd_try_df.columns = ["date", "usd_try_exchange_rate"]

# Convert the 'date' column from "dd-mm-yyyy" format to datetime format.
usd_try_df['date'] = pd.to_datetime(usd_try_df['date'], format='%d-%m-%Y')

# Plot the line chart

# Set the size of the plotting area.
plt.figure(figsize=(20, 8))

# Represent USD/TRY exchange rate data using a line chart.
plt.plot(usd_try_df["date"], usd_try_df["usd_try_exchange_rate"], linestyle='-', color='b')

# Add title and label the axes.
plt.title("USD/TRY Exchange Rate Over Time")
plt.xlabel("Date")
plt.ylabel("USD/TRY Exchange Rate")

# Rotate the date labels on the x-axis by 45 degrees for better readability.
plt.xticks(rotation=45)

# Adjust the layout for better visualization.
plt.tight_layout()

# Add grid lines to enhance data interpretation.
plt.grid(True)

# Save the plot as an image file.
plt.savefig("usd_try_exchange_rate_plot.png")