#!/bin/bash

# HTSLIB
wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 -O /tmp/htslib.tar.bz2
cd /tmp; tar xf htslib.tar.bz2; cd htslib-1.9; ./configure; make; make install

# SAMTOOLS
wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 -O /tmp/samtools.tar.bz2
cd /tmp; tar xf samtools.tar.bz2; cd samtools-1.9; ./configure; make; make install
