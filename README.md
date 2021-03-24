# Repeatmask pipeline

Masking of repeats in genome sequences.

Rough pipeline outline:

1. Run repeat modeler on fasta
2. Blast suspected repeats against public databases (NR, RFAM, Retro). Matches will not be masked as repeats.
3. Mask Repeats
