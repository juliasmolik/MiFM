from Bio import Entrez, SeqIO, AlignIO
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os


def fetch_seqs(csv_file):
    """
    Function used to download nucleotide sequences with a given ID from Genbank.
    It writes sequences of a given marker to a file in fasta format for selected species.
    
    :param csv_file: csv file containing the species names and sequence ID numbers of the selected markers
    """

    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    df = pd.read_csv(csv_file)
    Entrez.email = "A.N.Other@example.com"
    for marker in list(df.columns)[1:]: # without taxon column
        acc_numbers = list(df[marker])
        sequences = []
        for index, acc_number in enumerate(acc_numbers):
            if pd.notnull(acc_number):
                # download nucleotide sequence
                handle = Entrez.efetch(db="nucleotide", id=acc_number, rettype="fasta", retmode="text")
                record = SeqIO.read(handle, "fasta")
                sequences.append(SeqRecord(seq=record.seq, name = "", id="{}".format(list(df["Taxon"])[index].replace(" ", "_")), description=''))
        # saving to file
        with open(path+"{}.fasta".format(marker.lower()), "w") as fasta_file:
            SeqIO.write(sequences, fasta_file, "fasta")

    
fetch_seqs("./data/accesion_numbers.csv")