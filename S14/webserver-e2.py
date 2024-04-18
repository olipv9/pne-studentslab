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
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        num = 200

        # Check the request:
        if self.requestline.split(' ')[1] == '/blue.html':
            body = Path('blue.html').read_text()
        elif self.requestline.split(' ')[1] == '/pink.html':
            body = Path('pink.html').read_text()
        elif self.requestline.split(' ')[1] == '/green.html':
            body = Path('green.html').read_text()
        elif self.requestline.split(' ')[1] == '/' or self.requestline.split(' ')[1] == '/index.html':
            body = Path('index.html').read_text()
        else:
            body = Path('error.html').read_text()
            num = 404

        # Message to send back to the client
        # Generating the response message
        self.send_response(num)  # -- Status line: OK!

        # Define the content-type header: when deleted this also works (WHY)
        self.send_header('Content-Type',
                         'html')  # Value html when we want to show HTML look, use text/plain: just text.
        self.send_header('Content-Length', str(body.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(body.encode())

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
