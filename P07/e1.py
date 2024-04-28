import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINTS = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINTS + PARAMS
SEND_INFO = ENDPOINTS + PARAMS
print()
print(f'Server: {SERVER}\nURL: {URL}\n___________________________')

try:
    # To connect with the server:
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", SEND_INFO)

    # Get the response and read the data
    response = connection.getresponse()
    data = response.read().decode('utf-8')

    # Check the request status-> (status code must be = 200 for it to be successful)
    if response.status == 200:
        parsed_data = json.loads(data)
        print("Ping response: 200 OK")
        print('PING OK! Database running!')
    else:  # Whenever there exists a problem with the connection
        print(f"Error: {response.status} - {response.reason}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    connection.close()

