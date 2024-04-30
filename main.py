import requests
from datetime import datetime

USERNAME = "*********"
TOKEN = "************"
GRAPH_ID = "graph01"
# Below is another format for manually putting the time in the datetime object
time = datetime(year=2024, day=26, month=4)
time = datetime.now()
#Convert the above time format into a format requested by 'pixela'(yyyymmdd)
pixela_format_time = time.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_parameters)
# # Give back the response as a piece of text
# print(response.text)

# Creating the graph on pixela and authenticating ourselves using a 'Header'

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph01",
    "name": "Hours spent studying",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

main_url = "https://pixe.la/v1/users/master99/graphs/graph01.html"


## Using the 'POST' method to insert a value to the graph

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

value_parameters = {
    "date": pixela_format_time,
    "quantity": "2.5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=value_parameters, headers=headers)
print(response.text)
print(time)
print(pixela_format_time)


## Using the 'PUT' method to edit a pixel in 'pixela'

edit_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{pixela_format_time}"

edit_parameters = {
    "quantity": "7.5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=edit_endpoint, json=edit_parameters, headers=headers)
# print(response.text)


## Using the 'DELETE' method to delete a pixel in 'pixela'

delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{pixela_format_time}"

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)