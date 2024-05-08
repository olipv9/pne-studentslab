import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from useful_function import check_for_seq_errors, read_html_file

# Define the Server's port
PORT = 8080
num = 200
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def get_webpage_main(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Open the form1.html file
        # Read the index from the file
        try:
            if self.requestline.split(' ')[1] == '/':
                body = Path('html/index.html').read_text()

        except (IndexError, FileNotFoundError):
            body = Path('html/error.html').read_text()


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