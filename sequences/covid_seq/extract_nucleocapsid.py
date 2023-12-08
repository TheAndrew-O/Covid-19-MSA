"""
OR821857-OR823208 100 sequences
"""
from Bio import SeqIO

def extract_surface_glycoprotein_sequences(input_file, output_file):
    with open(input_file, 'r') as in_handle, open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(in_handle, 'fasta'):
            if 'nucleocapsid phosphoprotein' in record.description.lower():
                SeqIO.write(record, out_handle, 'fasta')

# Replace 'input.fasta' with the actual name of your FASTA file
input_file = 'sequences (1).fasta'

# Replace 'covid_nucleocapsid .fna' with the desired name for the output file
output_file = 'covid_nucleocapsid.fna'

extract_surface_glycoprotein_sequences(input_file, output_file)
