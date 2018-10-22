class Run():

    def run_all(options):

        #repeatmodeler_dir = RepeatModeler(options)
        blastNR(options, "repeatmodeler_dir")




import subprocess as sp
# out_file = open("{}/out.log".format(options.install_dir), 'w') # logging standard output
# err_file = open("{}/err.log".format(options.install_dir), 'w') # Logging standeard error

def call_sp(command):
    sp.call(command, shell = True)#, stdout = out_file, stderr = err_file)

def call_sp_retrieve(command):
    out, err = sp.Popen(command, shell = True, stdout = sp.PIPE).communicate()
    return out.decode()

def RepeatModeler(options):

    # Prepare and Build Genome database
    prepare_cmd = "cp {} {}".format(options.assembly, options.workdir)
    build_cmd = "cd {}; BuildDatabase -engine ncbi -n \"genome_db\" {}".format(options.workdir,
                                                                               options.assembly)
    call_sp(prepare_cmd)
    call_sp(build_cmd)


    # Run RepeatModeler
    repeatModeler_cmd = "cd {}; RepeatModeler -pa {} -database genome_db 2>&1 | tee RepeatModeler.stdout".format(
        options.workdir, options.n_treads)
    call_sp(repeatModeler_cmd)

    # Retrieve the workdir from RepeatModeler
    repeatModeler_workdir_cmd = "cat RepeatModeler.stdout | egrep \"Working directory:  .+\""
    repeatmodeler_dir = call_sp_retrieve(repeatModeler_workdir_cmd).split("  ")[1].strip("\n")

    return repeatmodeler_dir

def blastNR(options, repeatmodeler_dir):
     # Create folder structure
     create_folders_cmd = "cd {}; mkdir blastResults; cd blastResults; mkdir NR; mkdir RFAM; mkdir Retrotransposon".format(options.workdir)
