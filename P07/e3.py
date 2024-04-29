# In this exercise you have to program a client that connects to the /sequence/id endpoint and
# gets the sequence and description of the MIR633 gene.
import termcolor
import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINTS = '/sequence/id/'
gene_id = 'ENSG00000234389'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINTS + PARAMS
print(f'\nServer: {SERVER}\nURL: {URL}')
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


# MIR633 gene identifier
gene_id = "ENSG00000234389"
gene = 'MIR633'
# Get the sequence and description of the MIR633 gene
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
