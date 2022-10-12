# chdir into working directory
cd $JobWorkDir

# configure maple
maple config job.target

# run simulations
mpirun maple container run "/home/run/flashx_neumann -par_file job.input"
