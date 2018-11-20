#!/bin/bash

# Build bam2wig dependencies (htslib, bfctools, samtools)
git clone https://github.com/samtools/htslib.git /root/htslib
cd /root/htslib
autoheader
autoconf
./configure
make
make install
git clone https://github.com/samtools/bcftools.git /root/bcftools
cd /root/bcftools
autoheader
autoconf
./configure
make
make install
git clone https://github.com/samtools/samtools.git /root/samtools
cd /root/samtools
autoheader
autoconf -Wno-syntax
./configure
make
make install
export TOOLDIR="/root"

git clone https://github.com/Gaius-Augustus/Augustus /root/Augustus
cd /root/Augustus
mkdir bin
cd auxprogs/bam2wig
make

cd /root/Augustus
make
make install


# Configuration 
echo 'export AUGUSTUS_CONFIG_PATH=/root/Augustus/config'    >> ~/.bashrc
echo "export AUGUSTUS_BIN_PATH=/root/Augustus/bin"          >> ~/.bashrc
echo 'export AUGUSTUS_SCRIPTS_PATH=/root/Augustus/scripts'  >> ~/.bashrc
echo 'export PATH=$PATH:/root/Augustus/auxprogs/utrrnaseq/' >> ~/.bashrc
