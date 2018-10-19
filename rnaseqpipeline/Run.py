class Run():

    def run_all(options):

        RepeatModeler(options)




import subprocess as sp
out_file = open("{}/out.log".format(options.install_dir), 'w') # logging standard output
err_file = open("{}/err.log".format(options.install_dir), 'w') # Logging standeard error

def call_sp(command):
    sp.call(command, shell = True)#, stdout = out_file, stderr = err_file)

def RepeatModeler(options):
    print("hello boys")
    call_sp('ls')

    # Build Genome database
