From ubuntu:18.04

COPY . /app

# Install required packages
RUN sed 's/archive.ubuntu/nl.archive.ubuntu/g' /etc/apt/sources.list -i
RUN apt-get update
RUN apt-get install -y build-essential wget git autoconf cpanminus vim python3-pip

# Install dependencies for AUGUSTUS
RUN apt-get install -y libboost-iostreams-dev zlib1g-dev
RUN apt-get install -y libgsl-dev libboost-graph-dev libsuitesparse-dev liblpsolve55-dev libsqlite3-dev libmysql++-dev
RUN apt-get install -y libbamtools-dev
RUN apt-get install -y libboost-all-dev

# Install additional dependencies for htslib and samtools
RUN apt-get install -y libbz2-dev liblzma-dev
RUN apt-get install -y libncurses5-dev

# Install additional dependencies for bam2wig
RUN apt-get install -y libssl-dev libcurl3-dev


# Install conda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/Miniconda3-latest-Linux-x86_64.sh
RUN bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda
RUN echo 'export PATH=$PATH:/opt/miniconda/bin' >> ~/.bashrc

RUN /opt/miniconda/bin/conda install -y -c bioconda infernal=1.1.2

# Install additionall
RUN bash /app/install.sh
RUN bash /app/augustus.sh
RUN bash /app/braker.sh
#RUN bash /app/maker.sh
