#!/bin/bash

apt update

apt install -y python3-pip \
	build-essential \
    	libssl-dev \
	wget \
	cpanminus \
	vim
# CONDA
cd /tmp; wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
cd /tmp; bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda

echo 'export PATH=$PATH:/opt/miniconda/bin' >> ~/.bashrc
export PATH=$PATH:/opt/miniconda/bin

# HMMER
wget http://eddylab.org/software/hmmer/hmmer-2.3.2.tar.gz -O /tmp/hmmer.tar.gz
cd /tmp; tar xf hmmer.tar.gz
cd /tmp/hmmer-2.3.2; ./configure --enable-threads --enable-mpi; make; make install

# INFERNAL
conda install -y -c bioconda infernal=1.1.2 

# samtools -> currently using the aptitute version
#bash samtools.sh

pip3 install AnnotationPipeline

annotation_pipeline install pipeline --dir /opt -g True

#apt install -y augustus \
#       	       augustus-data \
#	       augustus-doc \
#	       bamtools \
#	       libbamtools-dev \
#	       samtools



# Genome Threader -> for braker2
cd /opt; http://genomethreader.org/distributions/gth-1.7.1-Linux_x86_64-64bit.tar.gz
cd /opt; tar xf gth-1.7.1-Linux_x86_64-64bit.tar.gz
echo 'export PATH=$PATH:/opt/gth-1.7.1-Linux_x86_64-64bit/bin >> ~/.bashrc'
echo 'export BSSMDIR=/opt/gth-1.7.1-Linux_x86_64-64bit/bin/bssm >> ~/.bashrc'
echo 'export GTHDATADIR=/opt/gth-1.7.1-Linux_x86_64-64bit/bin/gthdata >> ~/.bashrc'
echo 'export ALIGNMENT_TOOL_PATH=/opt/gth-1.7.1-Linux_x86_64-64bit/ >> ~/.bashrc'
