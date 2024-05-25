import http.client
import json


class GeneIdentifierClient:
    def __init__(self):
        self.server = 'rest.ensembl.org'
        self.endpoint = '/xrefs/symbol/homo_sapiens/'

    def get_gene_identifiers(self, genes):
        print(f'Dictionary of genes!\nThere are {len(genes)} genes in the dictionary\n')
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






