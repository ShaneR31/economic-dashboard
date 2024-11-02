import os
import requests
import pandas as pd

# Load the API key from environment variable
api_key = os.getenv('fred_api.env')

# Define FRED API base URL
base_url = 'https://api.stlouisfed.org/fred/series/observations'

# Function to fetch data for a specific series ID