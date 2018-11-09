#!/bin/bash

apt update

apt install -y python3-pip \
	build-essential \
    	libssl-dev \
	wget \
	cpanminus

pip3 install -y AnnotationPipeline

annotation_pipeline install pipeline --dir /opt

apt install -y augustus \
       	       augustus-data \
	       augustus-doc \
	       bamtools \
	       libbamtools-dev \
	       samtools


