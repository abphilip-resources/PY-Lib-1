import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'                       # URL to scrape from 
response = requests.get(url)                                                # Send a request to the website
soup = BeautifulSoup(response.text, 'lxml')                                 # Create a BeautifulSoup object
c = 1
pagination = soup.find('ul', class_='pagination')                           # Find the ul tag with class 'pagination'
pages = pagination.find_all('a', class_='page-link')                        # Find all the a tags with class 'page-link' in the ul tag
urls = ['']+[z.get('href') for z in pages if(z.text.isdigit())]             # Add the href attribute of all the a tags to the urls list

for z in urls:
    response = requests.get(url+z)                                          # Page URL to scrape from 
    soup = BeautifulSoup(response.text, 'lxml')                             # Create a BeautifulSoup object

    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')           # Find all the items in the current page
    for y in items:
        n = y.find('h4', class_='card-title').text.strip('\n')              # Find the name of the item
        p = y.find('h5').text                                               # Find the price of the item
        print('{}) Price: {}, Item Name: {}'.format(c, p, n))               # Print the item's name and price
        c+=1                                                                # Increment the item number