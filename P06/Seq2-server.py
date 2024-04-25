import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from function_result import get_result
from Seq1P03 import Seq

# Define the Server's port
PORT = 8080
num = 200
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
sequence = {'0': 'ATACCAGTAG', '1':'ACACGATAGACAAG', '2':'CATGGACGTGAAC', '3':'ACCACACAGGCCACGT', '4':'AGCCGTGACGTAGCA'}


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_average(dic_of_bases, s, base):
    num = dic_of_bases[base]
    average = (num * 100) / len(s)
    average = round(average, 2)
    return average, num

def check_for_seq_errors(seq):
    seq = seq.upper()
    seq_bases = ['A', 'C', 'G', 'T']
    valid = True
    for i in seq:
        if i not in seq_bases:
            print(f'The sequence given {seq} is not valid due to invalid characters.')
            valid = False
            break
    return valid

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
                quit_line = seq.split("\n")
                seq = "".join(quit_line[1:])
                body = body.render(context={'todisplay': seq, 'todisplay1': gene_opt})
            elif self.requestline.split(' ')[1].startswith('/operation?'):
                try:
                    seq = self.requestline.split(' ')[1].split('=')[1].split('&')[0]
                    check_valid = check_for_seq_errors(seq)
                    if not check_valid:
                        raise IndexError
                    option = self.requestline.split(' ')[1].split('=')[2]
                    body = read_html_file('operation.html')
                    if option == 'info':
                        body = body.render(context={'todisplay': seq, 'todisplay1': option, 'todisplay2': f'Total length: {len(seq)}',
                                                    'todisplay3':get_result(seq)})
                    elif option == "complementary":
                        comp_seq = Seq(seq)
                        comp_seq = comp_seq.complement()
                        body = body.render(context={'todisplay': seq, 'todisplay1': option, 'todisplay2': comp_seq, 'todisplay3':'' })
                    elif option == "reverse":
                        reverse_seq = Seq(seq)
                        reverse_seq = reverse_seq.rev_seq()
                        body = body.render(context={'todisplay': seq, 'todisplay1': option, 'todisplay2': reverse_seq, 'todisplay3':''})
                except IndexError:
                    body = Path('html/error.html').read_text()
                    num = 404
            else:
                body = Path('html/error.html').read_text()
                num = 404
        except FileNotFoundError:
            body = Path('error.html').read_text()
            num = 404

        # Generating the response message

        self.send_response(num)  # -- Status line: OK!

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