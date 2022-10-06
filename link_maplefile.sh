# chdir into directory containing the file
cd $JOB_FILEDIR

cd $JOB_FILEDIR/neumann && rm -f Maplefile && maple config $JOB_FILEDIR/Maplefile.simulation
cd $JOB_FILEDIR/outflow/buffer01 && rm -f Maplefile && maple config $JOB_FILEDIR/Maplefile.simulation
cd $JOB_FILEDIR/outflow/buffer10 && rm -f Maplefile && maple config $JOB_FILEDIR/Maplefile.simulation
cd $JOB_FILEDIR/outflow/buffer15 && rm -f Maplefile && maple config $JOB_FILEDIR/Maplefile.simulation
cd $JOB_FILEDIR/outflow/buffer20 && rm -f Maplefile && maple config $JOB_FILEDIR/Maplefile.simulation
