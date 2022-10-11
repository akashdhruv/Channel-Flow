# cache the value of current node directory
NodeDir=$PWD

# configure Maplefile
if [ $JobWorkDir != $NodeDir ]; then
	# configure Maplefile
	cd $JobWorkDir && maple config $NodeDir/Maplefile
fi

# run job
cd $JobWorkDir && mpirun maple container run "/home/run/flashx_outflow -par_file job.input"
