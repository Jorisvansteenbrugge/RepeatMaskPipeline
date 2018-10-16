

class Install():

    def verify_installation(options):
        print('veryifying install')





    def perform_installation(options):
        import subprocess as sp
        import os

        print('Performing installation in {} '.format(options.install_dir))

        FNULL = open(os.devnull, 'w')

        def RepeatModeler(options):
            print("Installing RepeatModeler")

            def RECON():
                # Check first if already installed
                if verify_RECON():
                    return
                print ("    Installing RECON...")
                recon_url = 'http://www.repeatmasker.org/RepeatModeler/RECON-1.08.tar.gz'
                download_cmd = 'wget {0} -O {1}/recon.tar.gz; cd {1}; tar xf recon.tar.gz;'.format(
                recon_url, options.install_dir
                )
                # Download and extract
                sp.call(download_cmd, shell=True, stdout=FNULL)

                # Building
                sp.call('cd {}/RECON-1.08/src; make; make install'.format(options.install_dir), shell = True)
                # Modify the REcon scrip to use the right paths
                sed_cmd = "sed -i 's+$path = \"\";+$path = {0}/RECON-1.08/bin+g' {0}/RECON-1.08/scripts/recon.pl".format(
                options.install_dir
                )
                sp.call(sed_cmd, shell=True, stdout=FNULL)
                    # Cleanup
                sp.call('rm {}/recon.tar.gz'.format(options.install_dir), shell=True, stdout=FNULL)

                #Add files to path
                sp.call("echo \'# RECON-1.08 installation dir\' >> ~/.bashrc; echo \'export PATH=$PATH:{0}/RECON-1.08/bin\' >> ~/.bashrc".format(options.install_dir),
                    shell = True,
                    stdout = FNULL)

            def RepeatScout():
                recon_url = 'http://www.repeatmasker.org/RepeatScout-1.0.5.tar.gz'
                download_cmd = 'wget {0} -O {1}/RepeatScout.tar.gz; cd {1}; tar xf RepeatScout.tar.gz;'.format(
                recon_url, options.install_dir
                )
                # Download and extract
                sp.call(download_cmd, shell=True, stdout=FNULL)
                # Building
                sp.call('cd {}/RepeatScout-1/ ; make'.format(options.install_dir),
                shell = True, stdout=FNULL)

                # Cleanup
                sp.call('rm {}/RepeatScout.tar.gz'.format(options.install_dir),
                shell=True, stdout=FNULL)
                bashrc = "echo export PATH=$PATH:{}/RepeatScout-1/ >> ~/.bashrc".format(options.install_dir)
                sp.call(bashrc, shell = True, stdout=FNULL)

            def TandenRepeatFinder():
                conda_channel = "conda config --add channels {}"
                sp.call(conda_channel.format('bioconda'),
                        shell = True, stdout=FNULL)
                sp.call(conda_channel.format('conda-forge'),
                        shell = True, stdout=FNULL)
                sp.call(conda_channel.format('WURnematology'),
                        shell = True, stdout=FNULL)
                sp.call("conda install -y tandemrepeatfinder",
                        shell = True, stdout=FNULL)

            def RMBlast():

                cmd = "wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-blast-2.6.0+-src.tar.gz -O {}/ncbi-blast.tar.gz".format(
                    options.install_dir)
                sp.call(cmd,
                    shell = True, stdout=FNULL)
                sp.call('tar xf ncbi-blast.tar.gz',
                    shell = True, stdout=FNULL)
                sp.call('wget http://www.repeatmasker.org/isb-2.6.0+-changes-vers2.patch.gz -O {}/isb-2.6.0+-changes-vers2.patch.gz'.format(
                options.install_dir),
                    shell = True, stdout=FNULL)
                sp.call('gunzip {}/isb-2.6.0+-changes-vers2.patch.gz'.format(options.install_dir),
                    shell = True, stdout=FNULL)
                sp.call("cd {}/ncbi-blast-2.6.0+-src ; patch -p1 < ../isb-2.6.0+-changes-vers2.patch".format(options.install_dir),
                    shell = True, stdout=FNULL)
                sp.call('cd {0}/ncbi-blast-2.6.0+-src/c++; ./configure --with-mt --prefix={0}/ncbi-blast-2.6.0+-src/ --without-debug'.format(
                options.install_dir),
                        shell = True, stdout=FNULL)
                sp.call('cd {0}/ncbi-blast-2.6.0+-src/c++; make; make install'.format(options.install_dir),
                        shell = True, stdout=FNULL)
            def RepeatMasker():
                sp.call('wget -c http://www.repeatmasker.org/RepeatMasker-open-4-0-7.tar.gz -O {}/RepeatMasker-open-4-0-7.tar.gz'.format(
                        options.install_dir),
                        shell = True, stdout=FNULL)
                sp.call('cd {}; tar xf RepeatMasker-open-4-0-7.tar.gz'.format(options.install_dir),
                        shell = True, stdout=FNULL)
                sp.call('cd RepeatMasker; ./configure --prefix=$(pwd)',
                        shell = True, stdout=FNULL)

            RECON()
            #RepeatScout()
            #TandenRepeatFinder()
            #RMBlast()
            #RepeatMasker()
        RepeatModeler(options)

def verify_RECON():
    import subprocess as sp

    try:
        out, err = sp.Popen('edgeredef', stdout = sp.PIPE, stderr = sp.PIPE).communicate()
        if b'usage' in out: # This check is only to be safe, it will not reach the else
            print('    Skipping RECON (already installed)...')
            return True
        else:
            return False
    except FileNotFoundError:
        return False
