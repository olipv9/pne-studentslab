import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
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

    if req_line.split('/')[2].startswith('A'):
        body = """
        <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Adenine<3</title>
      </head>
      <body style="background-color: lightpink;">
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
  <body style="background-color: turquoise;">
    <h1>Citosine</h1>
    <p>Letter: C</p>
    <p>Chemical formula: C4H5N3O</p>
    <a href="https://en.wikipedia.org/wiki/Citosine">More info</a>
  </body>
</html>
        """
    else:
        body = ''


    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


