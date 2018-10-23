#!/usr/bin/env python
import subprocess as sp
from Bio import SeqIO
from joblib import Parallel, delayed

class Blaster():

    def blastFasta(fasta_file, blast_type):
        records = list(SeqIO.parse(fasta_file, 'fasta'))



def blast(record, blast_type, database = 'nr', format_type = "Text", remote = "-remote"):

    blast_cmd = "{0} -database {1} {2} -query - ".format(blast_type, database, remote)

    p = sp.Popen(blast_cmd, stdin = sp.PIPE, stdout = sp.PIPE, shell = True)
    blast_out = p.communicate(input=record.seq)
    print(blast_out)
