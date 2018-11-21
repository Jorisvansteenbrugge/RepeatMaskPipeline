#!/bin/bash

# Install perl modules
cpanm File::Which
cpanm Bio::Root::Version
cpanm IO::All
cpanm IO::Prompt
cpanm DBD::SQLite
cpanm Perl::Unsafe::Signals
cpanm Bit::Vector
cpanm Inline::C
cpanm forks
cpanm forks::shared
cpanm Want
cpanm DBI

# Bioperl
cd /opt; git clone https://github.com/bioperl/bioperl-live
echo 'export PERL5LIB=$PERL5LIB:/opt/bioperl-live >> ~/.bashrc'
# NCBI blast
# should already be installed

# SNAP
wget http://korflab.ucdavis.edu/Software/snap-2013-11-29.tar.gz -O /opt/snap.tar.gz
cd /opt; tar xf snap.tar.gz; cd snap; make
echo 'export ZOE="/opt/snap/Zoe" >> ~/.bashrc'
echo 'export PATH=$PATH:/opt/snap >> ~/.bashrc'

# RepeatMasker should already be installed
wget http://ftp.ebi.ac.uk/pub/software/vertebrategenomics/exonerate/exonerate-2.2.0-x86_64.tar.gz -O /opt/exonerate.tar.gz
cd /opt; tar xf exonerate.tar.gz
echo 'export PATH=$PATH:/opt/exonerate-2.2.0-x86_64/bin >> ~/.bashrc'


wget http://www.bioinformatics.nl/~steen176/tools/maker-2.31.10.tgz -O /opt/maker.tgz
cd /opt; tar xf maker.tgz; cd maker/src; perl Build.PL; ./Build install
