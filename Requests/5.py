import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'                     # URL to scrape from
response = requests.get(url)                            # Send a request to the website
soup = BeautifulSoup(response.text, 'lxml')             # Create a BeautifulSoup object

q = soup.find_all("span", class_="text")                # Find all the quotes from span with class text
a = soup.find_all("small", class_="author")             # Find all the authors from small with class author
t = soup.find_all("div", class_="tags")                 # Find all the tags from div with class tags

for z in range(len(q)):
    print('{}.'.format(z+1), q[z].text)                 # Print the quotes
    print('-', a[z].text, end=' || ')                   # Print the authors
    tags = t[z].find_all('a', class_='tag')             # Find all the tags from a with class tag
    for y in tags: print(y.text, end='. ')              # Print the tags
    print("\n")