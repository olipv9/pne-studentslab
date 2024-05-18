import http.client
import json
from useful_function import get_len_percent

class Ensembl_server:
    def __init__(self, url):
        self.server = 'rest.ensembl.org'
        self.url = url

    def get_option1(self, message):
        name_list = []
        count = 0
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", self.url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))
            if response.status == 200:
                try:
                    if 0 <= int(message) <= len(data['species']):
                        for i in data['species']:
                            if i["division"] == "EnsemblVertebrates" and count != int(message):
                                count += 1
                                name = i["display_name"]
                                name_list.append(name)
                            elif count == int(message):
                                break
                        return len(data['species']), name_list
                    else:
                        print(f'Limit must be a number within the range!')
                except (TypeError, ValueError):
                    print(f'Limit must be an integer number!')
            else:
                print(f"Error: {response.status} - {response.reason}")

        finally:
            if connection:
                connection.close()

    def get_option2(self):
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", self.url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))
            if response.status == 200:
                karyotype_list = data['karyotype']
                return karyotype_list
            else:
                print(f"Error: {response.status} - {response.reason}")
        except UnboundLocalError:
            print(f'That specie is not within the ensembl database, try again with a valid option!')
        except Exception as e:
            print(f"An error occurred: -> {e}")

    def get_option3(self, c_num):
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", self.url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))
            if response.status == 200:
                main_list = data['top_level_region']
                for i in main_list:
                    if i['name'] == c_num:
                        final_length = i['length']
                return final_length
            else:
                print(f"Error: {response.status} - {response.reason}")

        except UnboundLocalError:
            print(f'That specie is not within the ensembl database, try again with a valid option!')
        except Exception as e:
            print(f"An error occurred: -> {e}")

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
                print(f"Error: {response.status} - {response.reason}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_gene_sequence(self, gene_id):
        self.url = f"/sequence/id/{gene_id}?content-type=application/json"
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", self.url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))

            # Check if the request (status code 200)
            if response.status == 200:
                sequence = data["seq"]
                return sequence
            else:
                print(f"Error: {response.status} - {response.reason}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_gene_info(self, gene_id):
        gene_info_url = f"/lookup/id/{gene_id}?content-type=application/json"
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", gene_info_url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))
            if response.status == 200:
                gene_info = {
                    "start": data['start'],
                    "end": data['end'],
                    "length": data['end'] - data['start'] + 1,
                    "chromosome_id": data['seq_region_name'],
                    "gene_id": data['id'],
                    "gene_name": data['display_name']
                }
                return gene_info
            else:
                print(f"Error: {response.status} - {response.reason}")
        except Exception as e:
            print(f"An error occurred: -> {e}")

    def get_genes_in_region(self):
        try:
            connection = http.client.HTTPSConnection(self.server)
            connection.request("GET", self.url)
            response = connection.getresponse()
            data = json.loads(response.read().decode('utf-8'))
            if response.status == 200:
                gene_names = []
                for gene in data:
                    if gene['feature_type'] == 'gene':
                        gene_names.append(gene.get('external_name', gene['id']))
                # for gene in data:
                    # if gene['feature_type'] == 'gene':
                    #     gene_names.append(gene['external_name'])
                return gene_names
            else:
                print(f"Error: {response.status} - {response.reason}")
                return None
        except Exception as e:
            print(f"An error occurred: -> {e}")
            return None


