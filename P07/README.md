## Practice 7
##### Exercise 1: 
The request() method is used to send an HTTP request to the server

    - Method: 
    This is the HTTP method to be used in the request.
    -URL: 
    The URL which will be used to make the request.

This is the same as making a GET request to the full URL. (since the request will 
be done to the SERVER which has been previously stated ). 

    - 'connection = http.client.HTTPConnection(SERVER)'
    - 'connection.request("GET", ENDPOINT + PARAMS)'
