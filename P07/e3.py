import http.client
import json
import termcolor
from e2_class import GeneIdentifierClient

# Intro info:
SERVER = 'rest.ensembl.org'
ENDPOINTS = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINTS + PARAMS
gene = 'MIR633'
print(f'\nServer: {SERVER}\nURL: {URL}')

# Get id:
gene_client = GeneIdentifierClient()
genes = ['MIR633']
gene_id_dict = gene_client.get_gene_identifiers(genes)
gene_id = gene_id_dict[gene]

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
sequence, description = get_gene_sequence(gene_id)

if sequence is not None and description is not None:
    termcolor.cprint(f'Gene: ', 'yellow', end='')
    print(gene)
    termcolor.cprint(f'Description: ', 'yellow', end='')
    print(description)
    termcolor.cprint(f'Sequence: ', 'yellow', end='')
    print(sequence)

else:
    print("Failed to retrieve gene sequence and description.")