import http.client
import json
from Bio.Seq import Seq


class GeneAnalyzer:
    def __init__(self):
        self.server = 'rest.ensembl.org'
        self.endpoint = '/sequence/id/'

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

    def analyze_gene_sequence(self, gene_name):
        gene_id = self.get_gene_id(gene_name)
        if gene_id:
            sequence, description = self.get_gene_sequence(gene_id)
            if sequence:
                # Create Seq object
                seq_obj = Seq(sequence)

                # Calculate length and base counts
                total_length = len(seq_obj)
                base_counts = seq_obj.count_per_letter()

                # Calculate percentage of each base
                total_bases = sum(base_counts.values())
                base_percentages = {base: count / total_bases * 100 for base, count in base_counts.items()}

                # Calculate most frequent base
                most_frequent_base = max(base_counts, key=base_counts.get)

                # Print gene information
                print(f"Gene Name: {gene_name}")
                print(f"Description: {description}")
                print(f"Total Length: {total_length}")
                print(f"Number of Bases: {total_bases}")
                print("Percentage of Each Base:")
                for base, percentage in base_percentages.items():
                    print(f"{base}: {percentage:.2f}%")
                print(f"Most Frequent Base: {most_frequent_base}")
            else:
                print("Failed to retrieve gene sequence.")
        else:
            print(f"Gene '{gene_name}' not found.")

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


# Usage
gene_analyzer = GeneAnalyzer()
gene_name = input("Enter the gene name: ")
gene_analyzer.analyze_gene_sequence(gene_name)
# Now that we can get genes from the server, it is time to do some calculations with them. We will use the Seq Class we created some assignments ago.

# The program should ask the user to enter the gene name and then get the gene from the server, print the gene's name,
# its description (same as exercise 3), the total length, the number of bases, the percentage of each base and the most frequent base in the sequence.

import http.client
import json
import termcolor
from e2_class import GeneIdentifierClient
from Seq1 import Seq

# Get the gene:
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


# Get id:
gene_client = GeneIdentifierClient()
gene = [gene_name.upper()]
gene_id_dict = gene_client.get_gene_identifiers(gene)
gene_id = gene_id_dict[gene_name]

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
    print(gene_name)
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
    print(seq.most_freq_base())
else:
    print("Failed to retrieve gene sequence and description.")














