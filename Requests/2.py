import os
import csv
import json
import requests
from bs4 import BeautifulSoup

# Loading variable from .env
from dotenv import load_dotenv
load_dotenv()
api=os.getenv('API_KEY')

# API JSON --> CSV
weather,locations = [],['Bengaluru','Hyderabad','Pune','Chennai','Delhi']
for z in range(len(locations)):
    city = {}                                     # Create a dictionary for each location
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(locations[z],api))
    city['City'] = locations[z]
    city['Latitude'] = r.json()['coord']['lat']
    city['Longitude'] = r.json()['coord']['lon']
    city['Weather'] = r.json()['weather'][0]['description']
    city['Temp'] = r.json()['main']['temp']
    city['Pressure'] = r.json()['main']['pressure']
    city['Humidity'] = r.json()['main']['humidity']
    city['Wind speed'] = r.json()['wind']['speed']
    city['HTTP Status Code'] = r.json()['cod']
    weather.append(city)                          # Append each dictionary to the list

# Write weather to CSV
with open('weather.csv', 'w', newline='') as f:
    w = csv.DictWriter(f,city.keys())
    w.writeheader()                               # Write the topics as the header
    for z in weather: w.writerow(z)               # Write each location to the CSV file

# HTML BS4 --> CSV
quotes=[]  
r = requests.get("http://www.values.com/inspirational-quotes")
soup = BeautifulSoup(r.content, 'html5lib') 
r.close()
# print(r.content)                                --> Raw HTML Content
# print(soup.prettify())                          --> Prettified HTML5 Content

# Deriving quotes from the prettified HTML5 Content
t = soup.find('div', attrs = {'id':'all_quotes'}) 
# Finding all the divs with ID = 'all_quotes'
for z in t.findAll('div', attrs = 
    {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}                                    # Create a dictionary for each quote
    quote['Theme'] = z.h5.text                    # Quote's theme found at heading 5
    quote['URL'] = z.a['href']
    quote['IMG'] = z.img['src']
    quote['Quote'] = z.img['alt'].split(" #")[0]
    quotes.append(quote)                          # Append each dictionary to the list

# Write quotes to CSV
with open('quotes.csv', 'w', newline='') as f:
    w = csv.DictWriter(f,quote.keys())
    w.writeheader()                               # Write the topics as the header
    for z in quotes: w.writerow(z)                # Write each quote to the CSV file