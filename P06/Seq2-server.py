import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Open the form1.html file
        # Read the index from the file
        try:
            if self.requestline.split(' ')[1] == '/':
                body = Path('html/index.html').read_text()
            elif self.requestline.split(' ')[1] == '/ping?':
                body = Path('html/ping.html').read_text()
            elif self.requestline.split(' ')[1] == '/get?':
                body = '''<!DOCTYPE html>
                <html lang="en" dir="ltr">
                  <head>
                    <meta charset="utf-8">
                    <title> GET </title>
                  </head>
                  <body style="background-color: white;">
                    <h1> The sequence number'''+ i +''' </h1>
                    <p> ''' + sequence[i] + ''' </p>
                    <a href="/"> [Main page] </a>
                  </body>
                </html>'''
            else:
                body = Path('html/error.html').read_text()
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