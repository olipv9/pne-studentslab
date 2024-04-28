# Create a dictionary called "genes" that contains both the name of the genes and their identifiers.
# The program should print all the entries in the dictionary along with their identifiers:
import termcolor
import http.client
import json


# Define the server and endpoint
SERVER = 'rest.ensembl.org'
ENDPOINT = '/xrefs/symbol/homo_sapiens/'

# Define the list of genes
genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

# Create a dictionary to store gene identifiers
gene_identifiers = {}

# Iterate over genes and make requests for each gene
for gene in genes:
    # Establish connection with the server
    connection = http.client.HTTPSConnection(SERVER)

    try:
        # Send GET request to Ensembl REST API endpoint for the gene
        connection.request("GET", ENDPOINT + gene + "?content-type=application/json")

        # Get the response
        response = connection.getresponse()

        # Read and parse the JSON response
        data = json.loads(response.read().decode('utf-8'))

        # Check if the request was successful (status code 200)
        if response.status == 200:
            # Extract the stable identifier (gene id) from the first result
            gene_id = data[0]["id"]

            # Store the gene identifier in the dictionary
            gene_identifiers[gene] = gene_id
        else:
            print(f"Error: {response.status} - {response.reason} for gene {gene}")

    except Exception as e:
        print(f"An error occurred: gene {gene} -> {e}")

    finally:
        # Close the connection
        connection.close()

# Print gene identifiers
for gene, s_identifier in gene_identifiers.items():
    termcolor.cprint(f'{gene}: ', 'green', end='')
    print(f'-----> {s_identifier}')

