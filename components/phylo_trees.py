from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import numpy as np
import matplotlib.pyplot as plt
from Bio import Phylo
from Bio import SeqIO
from io import StringIO
import sys
import csv

def main():
    with open("/home/andrew/5481/5481_proj/sequences/covid_spikes_msa_muscle_clustal.aln", "r") as fp:
        align = AlignIO.read(fp,"clustal")
    
    #align = AlignIO.read("/home/andrew/5481/5481_proj/sequences/msa.fna", "fasta")

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(align)
    #print(dm)
    
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)
    Phylo.write(tree, 'tree_spike.txt', 'newick')

    fig = plt.figure(dpi=100)
    axes = fig.add_subplot(1,1,1)
    fig1 = plt.gcf()
    plt.show()
    Phylo.draw(tree, branch_labels=None)


if __name__ == "__main__":
    main()