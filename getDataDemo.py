import quandl

# Pandas dataframe is used by default
import pandas as pd

# Get and set api key
file = open("quandlapi.secret", "r")
api_key = file.readline()
quandl.ApiConfig.api_key = api_key


# Get sentiment data from FB tick by month
df = quandl.get('NS1/FB_US', start_date='2017-10-23', end_date='2018-10-23' )

print(df)
