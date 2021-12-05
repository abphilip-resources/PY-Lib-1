import requests
# Syntax --> requests.OPERATION(url, params={key: value}, args)

# Print available methods   -->     print(dir(r))
# Print Guide for methods   -->     print(help(r))
# Print Headers             -->     print(r.headers)
# Print Status Code         -->     print(r.status_code)
# Print Content of Response -->     print(r.content)
# Print Text of Response    -->     print(r.text)
# Print URL of Response     -->     print(r.url)

# Important: Actions and Resources will not be updated on the server 

# GET Method                --> Receive resource from server
r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(r.json())
print("HTTP Status Code:",r.status_code,"\n")      # 200 if successful
r.close()

# POST Method               --> Add new resource to server
data = {"userId": 1, "title": "Buy milk", "completed": False}
r = requests.post("https://jsonplaceholder.typicode.com/todos",json=data)
print(r.json())
print("HTTP Status Code:",r.status_code,"\n")      # 201 if added
r.close()

# PUT Method                --> Edit existing resources in server
data = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': True}
r = requests.put("https://jsonplaceholder.typicode.com/todos/1",json=data)
print(r.json())
print("HTTP Status Code:",r.status_code,"\n")      # 200 if modified
r.close()

# PATCH Method              --> Modify value of a specific fields in a resource
data = {'title': 'Clean Garage', 'completed': True}
r = requests.patch("https://jsonplaceholder.typicode.com/todos/1",json=data)
print(r.json())
print("HTTP Status Code:",r.status_code,"\n")      # 200 if modified
r.close()

# DELETE Method             --> Delete existing resources in server
r = requests.delete("https://jsonplaceholder.typicode.com/todos/1",json=data)
print(r.json())
print("HTTP Status Code:",r.status_code,"\n")      # 200 if deleted
r.close()

# Real World Application of Requests
r = requests.get('https://api.github.com/users/allenalvin333')
print("Working at:", r.json()['company'])
print("Website:", r.json()['blog'])
print("HTTP Status Code:",r.status_code,"\n")      # 200 if successful
r.close()