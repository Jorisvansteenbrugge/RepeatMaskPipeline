# Genome Threader -> for braker2 
cd /opt; wget http://genomethreader.org/distributions/gth-1.7.1-Linux_x86_64-64bit.tar.gz 
cd /opt; tar xf gth-1.7.1-Linux_x86_64-64bit.tar.gz 
echo 'export PATH=$PATH:/opt/gth-1.7.1-Linux_x86_64-64bit/bin' >> ~/.bashrc 
echo 'export BSSMDIR=/opt/gth-1.7.1-Linux_x86_64-64bit/bin/bssm' >> ~/.bashrc 
echo 'export GTHDATADIR=/opt/gth-1.7.1-Linux_x86_64-64bit/bin/gthdata' >> ~/.bashrc 
echo 'export ALIGNMENT_TOOL_PATH=/opt/gth-1.7.1-Linux_x86_64-64bit/' >> ~/.bashrc 
