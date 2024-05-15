import http.client
import json


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




