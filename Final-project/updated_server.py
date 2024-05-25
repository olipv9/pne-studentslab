import http.server
import json
import socketserver
import termcolor
from pathlib import Path
from useful_function import print_out_list, read_html_file, get_len_percent
from ensmbl_class_update import Ensembl_server2, get_scientific_name

# Define the Server's port
PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        num = 200
        content_type = 'text/html'
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Open the form1.html file
        # Read the index from the file
        try:
            request_path = self.requestline.split(' ')[1]

            if request_path == '/':
                body = Path('html/index.html').read_text()

            elif request_path.startswith('/listSpecies'):
                species_dict = {}
                message = request_path.split('/')[-1].split('=')[1].split('&')[0]
                option_1 = Ensembl_server2('/info/species?content-type=application/json')
                length, names_list = option_1.get_option1(message)
                if request_path.endswith('json=1'):
                    content_type = 'application/json'
                    species_dict['species'] = names_list
                    body = json.dumps(species_dict)
                else:
                    if length and names_list:
                        body = read_html_file('species_num.html')
                        body = body.render(context={'todisplay1': length, 'todisplay2': message,
                                                'todisplay3': f' {print_out_list(names_list)}'})

                    else:
                        raise FileNotFoundError

            elif request_path.startswith('/karyotype'):
                message = request_path.split('/')[-1].split('=')[1].split('&')[0]
                species_name = message.replace('+', ' ')
                species_name = get_scientific_name(species_name)
                option_2 = Ensembl_server2(f'/info/assembly/{species_name}?content-type=application/json')
                karyotype = option_2.get_option2()
                if request_path.endswith('json=1'):
                    content_type = 'application/json'
                    body = json.dumps(karyotype)
                elif karyotype:
                    body = read_html_file('karyotype.html')
                    body = body.render(context={'todisplay1': f' {print_out_list(karyotype)}'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/chromosomeLength'):
                message1 = request_path.split('/')[-1].split('=')[1].split('&')[0]
                chromosome = request_path.split('/')[-1].split('=')[-1]
                if request_path.split('=')[1].startswith('&') or request_path.split('=')[-1] == '':
                    body = Path('html/specific_error.html').read_text()
                    num = 400
                else:
                    species_name = message1.replace('+', '_')
                    option_3 = Ensembl_server2(f'/info/assembly/{species_name}?content-type=application/json')
                    length_chrom, chromosome_info = option_3.get_option3(chromosome)
                    if request_path.endswith('json=1'):
                        content_type = 'application/json'
                        body = json.dumps(chromosome_info)
                    elif length_chrom:
                        body = read_html_file('chrom_len.html')
                        body = body.render(context={'todisplay1': f' {length_chrom}'})
                    else:
                        raise FileNotFoundError

            elif request_path.startswith('/geneSeq'):
                gene = request_path.split('/')[-1].split('=')[1].split('&')[0].upper()
                option_4 = Ensembl_server2(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_4.get_gene_id(gene)
                gene_seq, data = option_4.get_gene_sequence(gene_id)
                if request_path.endswith('json=1'):
                    content_type = 'application/json'
                    body = json.dumps(data)
                elif gene_seq:
                    body = read_html_file('geneSeq.html')
                    body = body.render(context={'todisplay1': f' {gene}', 'todisplay2': f' {gene_seq}'})
                else:
                    raise FileNotFoundError

            elif request_path.startswith('/geneInfo'):
                gene = request_path.split('/')[-1].split('=')[1].split('&')[0].upper()
                option_5 = Ensembl_server2(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_5.get_gene_id(gene)
                gene_info_dict = option_5.get_gene_info(gene_id)
                if request_path.endswith('json=1'):
                    content_type = 'application/json'
                    body = json.dumps(gene_info_dict)
                elif gene_info_dict:
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
                gene = request_path.split('/')[-1].split('=')[1].split('&')[0].upper()
                option_6 = Ensembl_server2(f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json)")
                gene_id = option_6.get_gene_id(gene)
                gene_seq, data = option_6.get_gene_sequence(gene_id)
                total_length, gene_average_dict = get_len_percent(gene_seq)
                if request_path.endswith('json=1'):
                    content_type = 'application/json'
                    gene_average_dict['total_length'] = total_length
                    body = json.dumps(gene_average_dict)
                elif total_length:
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
                    num = 400
                else:
                    chromosome = request_path.split('=')[1].split('&')[0]
                    start = int(request_path.split('=')[2].split('&')[0])
                    end = int(request_path.split('=')[3].split('&')[0])
                    chromosome = chromosome.replace('+', '_')
                    option_7 = Ensembl_server2(f'/overlap/region/homo_sapiens/{chromosome}:{start}-{end}?feature=gene'
                                              f';content-type=application/json')
                    genes_region = option_7.get_genes_in_region()
                    if request_path.endswith('json=1'):
                        content_type = 'application/json'
                        body = json.dumps({'chromosome': chromosome, 'start':start, 'end':end, 'genes': genes_region})
                    elif genes_region:
                        body = read_html_file('geneList.html')
                        body = body.render(context={'todisplay1': f' {chromosome}: start ({start}) &rarr; end ({end})',
                                                    'todisplay2': f'{print_out_list(genes_region)}'})
                    else:
                        raise FileNotFoundError

            else:
                body = Path('html/error.html').read_text()
                num = 404
        except (FileNotFoundError, TypeError, IndexError, ValueError) as e:
            body = Path('html/error.html').read_text()
            num = 404
        except Exception as e:
            body = Path('html/error.html').read_text()
            num = 404
            print(f'An unexpected error occurred: {e}')

        # Generating the response message
        self.send_response(num)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', content_type)
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
