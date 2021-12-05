import requests
import json

url = 'https://api.upcitemdb.com/prod/trial/lookup'     # URL to scrape from
p = {'upc': '0885909950805'}                            # Parameters to send
response = requests.get(url, params=p)                  # Send a request to the website
data = json.loads(response.content)                     # Load the response content into a variable          
print(data['items'][0]['title'])                        # Print the title of the first item