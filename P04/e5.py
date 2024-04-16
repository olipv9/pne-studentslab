import socket
import termcolor


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client4(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)
    # This new contents are written in HTML language
    if req_line.split('/')[2].startswith('A'):
        body = """
        <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Adenine<3</title>
      </head>
      <body style="background-color: lightgreen;">
        <h1>Adenine</h1>
        <p>Letter: A</p>
        <p>Chemical formula: C5H5N5</p>
        <a href="https://en.wikipedia.org/wiki/Adenine">More info</a>
      </body>
    </html>
        """
    elif req_line.split('/')[2].startswith('C'):
        body = """
        <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Citosine<3</title>
      </head>
      <body style="background-color: yellow;">
        <h1>Citosine</h1>
        <p>Letter: C</p>
        <p>Chemical formula: C4H5N3O</p>
        <a href="https://en.wikipedia.org/wiki/Cytosine">More info</a>
      </body>
    </html>
        """
    elif req_line.split('/')[2].startswith('T'):
        body = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Thymine<3</title>
  </head>
  <body style="background-color: lightpink;">
    <h1>Thymine</h1>
    <p>Letter: T</p>
    <p>Chemical formula: C5H6N2O2 </p>
    <a href="https://en.wikipedia.org/wiki/Thymine">More info</a>
  </body>
</html>'''
    elif req_line.split('/')[2].startswith('G'):
        body = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Guanine<3</title>
  </head>
  <body style="background-color: turquoise;">
    <h1>Guanine</h1>
    <p>Letter: G</p>
    <p>Chemical formula: C5H5N5O</p>
    <a href="https://en.wikipedia.org/wiki/Guanine">More info</a>
  </body>
</html>'''

    else:
        body = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Error</title>
  </head>
  <body style="background-color: red;">
    <h1>ERROR</h1>
    <p>Resource not available</p>
  </body>
</html>'''

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print(" Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client4(cs)

        # -- Close the socket
        cs.close()

