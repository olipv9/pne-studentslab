# Create a dictionary called "genes" that contains both the name of the genes and their identifiers.
# The program should print all the entries in the dictionary along with their identifiers:
import termcolor
import http.client
import json


# Define the server and endpoint
SERVER = 'rest.ensembl.org'
ENDPOINT = '/xrefs/symbol/homo_sapiens/'
PARAMS = '?content-type=application/json'
# Define the list of genes
genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = {}


for gene in genes:
    try:
        # Establish connection with the server, and send GET request to Ensembl REST API endpoint for the gene
        connection = http.client.HTTPSConnection(SERVER)
        connection.request("GET", ENDPOINT + gene + PARAMS)

        # Get the response
        response = connection.getresponse()
        data = json.loads(response.read().decode('utf-8'))

        # Check if the request:
        if response.status == 200:
            if gene == genes[0]:
                print(f'Dictionary of genes!\nThere are {len(genes)} genes in the dictionary\n')
            # Obtain the stable identifier (gene id) from the dict they offer:
            gene_id = data[0]["id"]
            gene_identifiers[gene] = gene_id
        else:
            print(f"Error: {response.status} - {response.reason}: gene {gene}")

    except Exception as e:
        print(f"An error occurred: gene {gene} -> {e}")

    finally:
        # Close the connection
        connection.close()


for gene, s_identifier in gene_identifiers.items():
    termcolor.cprint(f'{gene}: ', 'green', end='')
    print(f'-----> {s_identifier}')

