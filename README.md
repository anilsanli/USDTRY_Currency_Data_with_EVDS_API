# TCMB EVDS API Data Retrieval Project

This project demonstrates how to retrieve historical Dollar to Turkish Lira (USD/TRY) exchange rate data using the TCMB (Central Bank of the Republic of Turkey) EVDS (Electronic Data Delivery System) API. The retrieved data is then visualized as a line chart. The script fetches exchange rate data within a specified date range and uses the obtained data for plotting.

## Prerequisites
* Python 3.x
* Required Python packages: pandas, matplotlib, evds
You can install the necessary packages using the following command:

pip install pandas matplotlib evds

## Usage
* Clone this repository or download the script file.
* Obtain your EVDS API key from TCMB and save it in a file named tcmb_evds_api_key.txt.
* Modify the script exchange_rate_plot.py to customize the date range and other parameters for data retrieval, if needed.
*Run the script:

python exchange_rate_plot.py

* The script will retrieve the exchange rate data and create a line chart to visualize it. The chart will be displayed on the screen and saved as an image file named usd_try_exchange_rate_plot.png.

## Customization
* Edit the exchange_rate_plot.py script to modify the startdate, enddate, and other parameters as required for your specific data retrieval needs.
* To change the output image file name and format, modify the argument of the plt.savefig() function in the script.

# DON'T FORGET TO USE YOUR OWN API KEY

# Author
* Anıl Şanlı

[LinkedIn](https://www.linkedin.com/in/anilsanli/)

[Kaggle](https://www.kaggle.com/sanlian)

[Medium](https://medium.com/@sanlian)

