#!/usr/bin/env python

from Bio import SeqIO
from joblib import Parallel, delayed
import multiprocessing
import subprocess as sp
import random
import time


class Blaster():

    def blastFasta(fasta_file, blast_type, n_threads, database = 'nr', remote = '-remote'):
        records = list(SeqIO.parse(fasta_file, 'fasta'))

        results = Parallel(n_jobs = n_threads)(delayed(blast(i, blast_type, database)) (i) for i in records)
        print(results)



def blast(record, blast_type, database = 'nr', remote = "-remote"):

    blast_cmd = "{0} -db {1} {2} -query - ".format(blast_type, database, remote)

    p = sp.Popen(blast_cmd, stdin = sp.PIPE, stdout = sp.PIPE, shell = True)
    blast_out = p.communicate(input=str(record.seq).encode())
    return blast_out
