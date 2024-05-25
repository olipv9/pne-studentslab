import http.client
import json
import termcolor
from e2_class import GeneIdentifierClient
from Seq1 import Seq

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




try:
    gene_name = str(input("Enter the gene name: ")).upper()
except Exception as e:
    print(f'An error occured: {e}')


# Intro info:
SERVER = 'rest.ensembl.org'
ENDPOINTS = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINTS + PARAMS
print(f'\nServer: {SERVER}\nURL: {URL}\n')


gene_client = GeneAnalyzer()
gene = gene_name.upper()
gene_id = gene_client.get_gene_id(gene)
seq, description = gene_client.get_gene_sequence(gene_id)
termcolor.cprint(f'Gene: ', 'yellow', end='')
print(gene_name)
termcolor.cprint(f'Description: ', 'yellow', end='')
print(description)

if seq and description:
    seq = Seq(seq)
    dict_bases = seq.seq_count()
    percen_a, num_a = seq.get_average('A')
    percen_c, num_c = seq.get_average('C')
    percen_t, num_t = seq.get_average('T')
    percen_g, num_g = seq.get_average('G')
    termcolor.cprint(f'Total length:', 'yellow', end='')
    print(f' {seq.len()}\n\t- A: {num_a} ({percen_a}%)\n\t- C: {num_c} ({percen_c}%)'
            f'\n\t- T: {num_t} ({percen_t}%)\n\t- G: {num_g} ({percen_g}%) ')
    termcolor.cprint(f'Most frequent base: ', 'yellow', end='')
    print(seq.most_freq_base())
else:
    print("Failed to retrieve gene sequence and description.")














