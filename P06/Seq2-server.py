import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j

# Define the Server's port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
sequence = {'0': 'ATACCAGTAG', '1':'ACACGATAGACAAG', '2':'CATGGACGTGAAC', '3':'ACCACACAGGCCACGT', '4':'AGCCGTGACGTAGCA'}


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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
            elif self.requestline.split(' ')[1].startswith('/get?'):
                number = self.requestline.split(' ')[1].split('=')[1]
                body = read_html_file('get.html')
                body = body.render(context={'todisplay': sequence[number],'todisplay1': number })
            elif self.requestline.split(' ')[1].startswith('/gene?'):
                gene_opt = self.requestline.split(' ')[1].split('=')[1]
                body = read_html_file('gene.html')
                filename = '../sequences/' + str(gene_opt + '_sequence.fa')
                seq = Path(filename).read_text()
                body = body.render(context={'todisplay': seq, 'todisplay1': gene_opt})
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