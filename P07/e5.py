import http.client
import json
import termcolor
from e2_class import GeneIdentifierClient
from Seq1 import Seq

# Get the gene:
gene_dict = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

# Intro info:
SERVER = 'rest.ensembl.org'
ENDPOINTS = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINTS + PARAMS
print(f'\nServer: {SERVER}\nURL: {URL}\n')


# Get id:
gene_client = GeneIdentifierClient()
genes = gene_dict
gene_id_dict = gene_client.get_gene_identifiers(genes)

# Get the description and sequence:
    # 1st define the fucntion:

def get_gene_sequence(gene_id):
    try:
        connection = http.client.HTTPSConnection(SERVER)
        connection.request("GET", f"/sequence/id/{gene_id}?content-type=application/json")
        response = connection.getresponse()
        data = json.loads(response.read().decode('utf-8'))

        # Check if the request (status code 200)
        if response.status == 200:
            print(f"Ping response!: 200 OK\n")
            sequence = data["seq"]
            description = data["desc"]

            return sequence, description
        else:
            print(f"Error: {response.status} - {response.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()
        else:
            print(f"An error occurred")


    # Now we obtain the rest:
for gene in gene_id_dict:
    gene_id = gene_id_dict[gene]
    sequence, description = get_gene_sequence(gene_id)
    if sequence is not None and description is not None:
        termcolor.cprint(f'Gene: ', 'yellow', end='')
        print(gene)
        termcolor.cprint(f'Description: ', 'yellow', end='')
        print(description)
        seq = Seq(sequence)
        dict_bases = seq.seq_count()
        percen_a, num_a = seq.get_average('A')
        percen_c, num_c = seq.get_average('C')
        percen_t, num_t = seq.get_average('T')
        percen_g, num_g = seq.get_average('G')
        termcolor.cprint(f'Total length:', 'yellow', end='')
        print(f' {len(sequence)}\n\t- A: {num_a} ({percen_a}%)\n\t- C: {num_c} ({percen_c}%)'
                f'\n\t- T: {num_t} ({percen_t}%)\n\t- G: {num_g} ({percen_g}%) ')
        termcolor.cprint(f'Most frequent base: ', 'yellow', end='')
        print(f'{seq.most_freq_base()}\n_____________________')
    else:
        print("Failed to retrieve gene sequence and description.")

