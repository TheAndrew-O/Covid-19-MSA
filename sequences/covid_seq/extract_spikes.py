from Bio import SeqIO

def extract_surface_glycoprotein_sequences(input_file, output_file):
    with open(input_file, 'r') as in_handle, open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(in_handle, 'fasta'):
            if 'surface glycoprotein' in record.description.lower():
                SeqIO.write(record, out_handle, 'fasta')

# Replace 'input.fasta' with the actual name of your FASTA file
input_file = 'covid_gen.fasta'

# Replace 'covid_spike.fna' with the desired name for the output file
output_file = 'covid_spike.fna'

extract_surface_glycoprotein_sequences(input_file, output_file)
