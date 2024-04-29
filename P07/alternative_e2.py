import http.client
import json
import termcolor


class GeneIdentifierClient:
    def __init__(self):
        self.server = 'rest.ensembl.org'
        self.endpoint = '/xrefs/symbol/homo_sapiens/'

    def get_gene_identifiers(self, genes):
        gene_identifiers = {}
        for gene in genes:
            try:
                connection = http.client.HTTPSConnection(self.server)
                connection.request("GET", self.endpoint + gene + "?content-type=application/json")
                response = connection.getresponse()
                data = json.loads(response.read().decode('utf-8'))

                if response.status == 200:
                    gene_id = data[0]["id"]
                    gene_identifiers[gene] = gene_id
                else:
                    print(f"Error: {response.status} - {response.reason}: gene {gene}")

            except Exception as e:
                print(f"An error occurred: gene {gene} -> {e}")

            finally:
                if connection:
                    connection.close()

        return gene_identifiers


# Usage
gene_client = GeneIdentifierClient()
genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = gene_client.get_gene_identifiers(genes)

for gene, identifier in gene_identifiers.items():
    termcolor.cprint(f'{gene}: ', 'green', end='')
    print(f'-----> {identifier}')
