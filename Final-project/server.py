import http.server
import socketserver
import termcolor
from pathlib import Path
import os

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        try:
            request_path = self.requestline.split(' ')[1]
            if request_path == '/':
                body = Path('html/index.html').read_text()
            elif request_path.startswith('/number_1'):
                body = Path('html/species_num.html').read_text()
            elif request_path.startswith('/number_2'):
                body = Path('html/karyotype.html').read_text()
            elif request_path.startswith('/number_3'):
                if request_path.split('=')[1].startswith('&') or request_path.split('=')[-1] == '':
                    body = Path('html/specific_error.html').read_text()
                else:
                    body = Path('html/chrom_len.html').read_text()
            else:
                body = Path('html/error.html').read_text()
        except FileNotFoundError:
            body = Path('html/error.html').read_text()

        # Generating the response message

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body)))  # Length of body as string

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
