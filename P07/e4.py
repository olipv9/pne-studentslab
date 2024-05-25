import http.client
import json
import termcolor


class GeneAnalyzer:
    def __init__(self):
        self.server = 'rest.ensembl.org'
        self.endpoint = '/sequence/id/'

    def get_gene_id(self, gene_name):
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", f"/xrefs/symbol/homo_sapiens/{gene_name}?content-type=application/json")
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))

            if response.status == 200 and data:
                gene_id = data[0]["id"]
                return gene_id
            else:
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        finally:
            if connection:
                connection.close()
    def get_gene_sequence(self, gene_id):
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", f"{self.endpoint}{gene_id}?content-type=application/json")
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))

            if response.status == 200:
                sequence = data["seq"]
                description = data["desc"]
                return sequence, description
            else:
                print(f"Error: {response.status} - {response.reason}")
                return None, None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

        finally:
            if connection:
                connection.close()




















