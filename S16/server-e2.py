import http.server
import socketserver
import termcolor
from pathlib import Path
from blankspaces import blank_spaces

# Define the Server's port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Open the form1.html file
        # Read the index from the file
        try:
            if self.requestline.split(' ')[1] == '/':
                body = Path('form-2.html').read_text()
            elif self.requestline.count('=') == 1:
                msg = self.requestline.split('=')[1].replace('HTTP/1.1', '')
                msg = blank_spaces(msg)
                body = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title> Received message: </title>
                </head>
                <body style="background-color: turquoise;">
                    <h1> Received message: </h1>
                    <p>''' + msg + '''</p>
                    <a href="/"> [Main page] </a>
                </body>
                </html>'''
            elif self.requestline.count('=') == 2:
                msg = self.requestline.split('=')[1].split('&')[0].upper()
                msg = blank_spaces(msg)
                body = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Received message: </title>
</head>
<body style="background-color: turquoise ;">
    <h1> Received message: </h1>
    <p>''' + msg + '''</p>
    <a href="/"> [Main page] </a>
</body>
</html>'''
            else:
                body = Path('error.html').read_text()
        except FileNotFoundError:
            body = Path('error.html').read_text()

        # Generating the response message

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(body.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(body))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()