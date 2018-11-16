From ubuntu:18.04

COPY . /app

# Install required packages
RUN sed 's/archive.ubuntu/nl.archive.ubuntu/g' /etc/apt/sources.list -i
RUN apt-get update
RUN apt-get install -y build-essential wget git autoconf

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

RUN bash /app/install.sh

