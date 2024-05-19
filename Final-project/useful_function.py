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


def get_len_percent(sequence):
    final_average_dict = {}
    try:
        if sequence:
            total_length = len(sequence)
            base_count = {'A': sequence.count('A'), 'T': sequence.count('T'), 'C': sequence.count('C'),
                          'G': sequence.count('G')}
            for key, value in base_count.items():
                final_average_dict[key] = f'{round((value / total_length) * 100, 2)} %'
            return total_length, final_average_dict
        else:
            print("Could not retrieve gene sequence.")
    except ZeroDivisionError as e:
        print(f"An error occurred: -> {e}")


