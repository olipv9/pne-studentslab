import requests

BASE_URL = 'http://localhost:8080'

def homepage():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("GET json info!")
    else:
        print("Something went wrong!")


def list_species(number):
    url = f"{BASE_URL}/listSpecies?msg={number}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Species List (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch species list. Status code: {response.status_code}")


def karyotype(species):
    url = f"{BASE_URL}/karyotype?species={species}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Karyotype (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch karyotype. Status code: {response.status_code}")


def chromosome_length(species, chromosome):
    url = f"{BASE_URL}/chromosomeLength?species={species}&chromosome={chromosome}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Chromosome Length (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch chromosome length. Status code: {response.status_code}")


def gene_sequence(gene):
    url = f"{BASE_URL}/geneSeq?gene={gene}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Gene Sequence (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch gene sequence. Status code: {response.status_code}")


def gene_info(gene):
    url = f"{BASE_URL}/geneInfo?gene={gene}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Gene Info (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch gene info. Status code: {response.status_code}")


def gene_calc(gene):
    url = f"{BASE_URL}/geneCalc?gene={gene}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Gene Calc (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch gene calc. Status code: {response.status_code}")


def gene_list(chromosome, start, end):
    url = f"{BASE_URL}/geneList?chromosome={chromosome}&start={start}&end={end}"
    url += '&json=1'
    response = requests.get(url)
    if response.status_code == 200:
        print("Gene List (JSON):")
        print(response.json())
    else:
        print(f"Failed to fetch gene list. Status code: {response.status_code}")


homepage()
list_species('8')
karyotype('homo sapiens')
chromosome_length('homo sapiens', '1')
gene_sequence('BLAST')
gene_info('BLAST')
gene_calc('BLAST')
gene_list('1', 1000000, 2000000)
