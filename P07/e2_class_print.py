import termcolor
from e2_class import GeneIdentifierClient

gene_client = GeneIdentifierClient()
genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = gene_client.get_gene_identifiers(genes)

for gene, identifier in gene_identifiers.items():
    termcolor.cprint(f'{gene}: ', 'green', end='')
    print(f'-----> {identifier}')


