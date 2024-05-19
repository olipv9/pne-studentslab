import http.server
import socketserver
import termcolor
from pathlib import Path
from ensembl_class_server import Ensembl_server, get_scientific_name
from useful_function import print_out_list, read_html_file, get_len_percent

# Define the Server's port
PORT = 8080


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

            elif request_path.startswith('/listSpecies'):
                message = request_path.split('/')[-1].split('=')[1]
                option_1 = Ensembl_server('/info/species?content-type=application/json')
                length, names_list = option_1.get_option1(message)
                if length and names_list:
                    body = read_html_file('species_num.html')
                    body = body.render(context={'todisplay1': length, 'todisplay2': message,
                                                'todisplay3': f' {print_out_list(names_list)}'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/karyotype'):
                message = request_path.split('/')[-1].split('=')[1]
                species_name = message.replace('+', ' ')
                species_name = get_scientific_name(species_name)
                option_2 = Ensembl_server(f'/info/assembly/{species_name}?content-type=application/json')
                karyotype = option_2.get_option2()
                if karyotype:
                    body = read_html_file('karyotype.html')
                    body = body.render(context={'todisplay1': f' {print_out_list(karyotype)}'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/chromosomeLength'):
                message1 = request_path.split('/')[-1].split('=')[1].split('&')[0]
                chromosome = request_path.split('/')[-1].split('=')[-1]
                if request_path.split('=')[1].startswith('&') or request_path.split('=')[-1] == '':
                    body = Path('html/specific_error.html').read_text()
                else:
                    species_name = message1.replace('+', '_')
                    option_3 = Ensembl_server(f'/info/assembly/{species_name}?content-type=application/json')
                    length_chrom = option_3.get_option3(chromosome)
                    if length_chrom:
                        body = read_html_file('chrom_len.html')
                        body = body.render(context={'todisplay1': f' {length_chrom}'})
                    else:
                        raise FileNotFoundError
            elif request_path.startswith('/geneSeq'):
                gene = request_path.split('/')[-1].split('=')[1].upper()
                option_4 = Ensembl_server(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_4.get_gene_id(gene)
                gene_seq = option_4.get_gene_sequence(gene_id)
                if gene_seq:
                    body = read_html_file('geneSeq.html')
                    body = body.render(context={'todisplay1': f' {gene}', 'todisplay2': f' {gene_seq}'})
                else:
                    raise FileNotFoundError
            elif request_path.startswith('/geneInfo'):
                gene = request_path.split('/')[-1].split('=')[1].upper()
                option_5 = Ensembl_server(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_5.get_gene_id(gene)
                gene_info_dict = option_5.get_gene_info(gene_id)
                if gene_info_dict:
                    body = read_html_file('geneInfo.html')
                    body = body.render(context={'todisplay1': f' {gene_info_dict["gene_name"]}',
                                                'todisplay2': f'- <b>Start</b>: {gene_info_dict["start"]}<br>'
                                                              f'- <b>End</b>: {gene_info_dict["end"]}<br>'
                                                              f'- <b>Length</b>: {gene_info_dict["length"]}<br>'
                                                              f'- <b>Chromosome</b>: {gene_info_dict["chromosome_id"]}<br>'
                                                              f'- <b>Id</b>: {gene_info_dict["gene_id"]}<br>'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/geneCalc'):
                gene = request_path.split('/')[-1].split('=')[1].upper()
                option_6 = Ensembl_server(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_6.get_gene_id(gene)
                gene_seq = option_6.get_gene_sequence(gene_id)
                total_length, gene_average_dict = get_len_percent(gene_seq)
                if total_length:
                    body = read_html_file('geneCalc.html')
                    body = body.render(context={'todisplay1': f' {gene}', 'todisplay2': f' {total_length}<br>',
                                                'todisplay3': f'- <b>A</b>: {gene_average_dict["A"]}<br>'
                                                              f'- <b>C</b>: {gene_average_dict["C"]}<br>'
                                                              f'- <b>T</b>: {gene_average_dict["T"]}<br>'
                                                              f'- <b>G</b>: {gene_average_dict["G"]}<br>'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/geneList'):
                if (request_path.split('=')[1].startswith('&') or request_path.split('=')[2] == '&' or
                        request_path.split('=')[-1] == ''):
                    body = Path('html/specific_error.html').read_text()
                else:
                    chromosome = request_path.split('=')[1].split('&')[0]
                    start = int(request_path.split('=')[2].split('&')[0])
                    end = int(request_path.split('=')[-1])
                    chromosome = chromosome.replace('+', '_')
                    option_7 = Ensembl_server(f'/overlap/region/homo_sapiens/{chromosome}:{start}-{end}?feature=gene'
                                              f';content-type=application/json')
                    genes_region = option_7.get_genes_in_region()
                    if genes_region:
                        body = read_html_file('geneList.html')
                        body = body.render(context={'todisplay1': f' {chromosome}: start ({start}) &rarr; end ({end})',
                                                    'todisplay2': f'{print_out_list(genes_region)}'})
                    else:
                        raise FileNotFoundError

            else:
                body = Path('html/error.html').read_text()
        except (FileNotFoundError, TypeError, IndexError, ValueError):
            body = Path('html/error.html').read_text()
        except Exception as e:
            body = Path('html/error.html').read_text()
            print(f'An unexpected error occurred: {e}')

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body)))  # Length of body as string
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(body))


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
