#!/bin/bash



# HMMER
wget http://eddylab.org/software/hmmer/hmmer-2.3.2.tar.gz -O /tmp/hmmer.tar.gz
cd /tmp; tar xf hmmer.tar.gz
cd /tmp/hmmer-2.3.2; ./configure --enable-threads --enable-mpi; make; make install

# INFERNAL
conda install -y -c bioconda infernal=1.1.2 


pip3 install AnnotationPipeline

annotation_pipeline install pipeline --dir /opt -g True

