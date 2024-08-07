import requests

# Base URL of the API
base_url = 'https://66b1f1a01ca8ad33d4f5d5f2.mockapi.io/api/bankaccount'

# Specify query parameters
params = {'username': 'yelena.hansen'}
#params={'address':'Coimbatore'}

# Send a GET request with query parameters
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the fetched data
    print("Fetched Data:")
    print(data)
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve data. Status code: {response.status_code}")
