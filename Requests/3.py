import json
import requests
import pandas as pd

# JSON Handling with Requests
url = 'https://api.covid19api.com/summary'
response = requests.get(url).text                               # GET text
response_info = json.loads(response)                            # Convert text to Python dictionary
print(type(response_info))                                      # <class 'dict'>
response_info = requests.get(url).json()                        # GET JSON
print(type(response_info))                                      # <class 'dict'>
print()

# Python Dictionary to 2D Array
country_list = []
for country_info in response_info['Countries']:                 # Loop through each country
    country_list.append([country_info['Country'],               # Add country name
    country_info['TotalConfirmed']])                            # Add total confirmed cases
for z in range(5): print(country_list[z])                       # Print first 5 countries
print()

# 2D Array to DataFrame 
country_df = pd.DataFrame(data=country_list,                    # Create DataFrame
columns=['Country', 'Total_Confirmed'])                         # Set column names
print(country_df.head(5))                                       # Print first 5 rows
print()

# Creating session objects with Requests
s = requests.Session()                                          # Create session object
s.get('https://httpbin.org/cookies/set/sessioncookie/allen')    # SET cookie
r = s.get('https://httpbin.org/cookies')                        # GET cookies
print(r.json()['cookies'])                                      # Print cookies