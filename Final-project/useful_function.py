import jinja2 as j
from pathlib import Path

def read_html_file(filename):
    try:
        contents = Path("html/" + filename).read_text()
        contents = j.Template(contents)
    except FileNotFoundError:
        print(f'The file does not exits')
        contents = None
    return contents


def check_for_seq_errors(seq):
    seq = seq.upper()
    seq_bases = ['A', 'C', 'G', 'T']
    valid = True
    for i in seq:
        if i not in seq_bases:
            print(f'The sequence given {seq} is not valid due to invalid characters.')
            valid = False
            break
    return valid


def print_out_list(enu_list):
    html = "<ul>"
    for index, item in enumerate(enu_list):
        html += f"<li>{item}</li>"
    html += "</ul>"
    return html
