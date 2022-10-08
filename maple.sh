# chdir into directory containing the file
cd $JOB_TREEDIR

cd $JOB_TREEDIR/neumann && rm -f Maplefile && maple config $JOB_TREEDIR/Maplefile.simulation
cd $JOB_TREEDIR/outflow/buffer01 && rm -f Maplefile && maple config $JOB_TREEDIR/Maplefile.simulation
cd $JOB_TREEDIR/outflow/buffer10 && rm -f Maplefile && maple config $JOB_TREEDIR/Maplefile.simulation
cd $JOB_TREEDIR/outflow/buffer15 && rm -f Maplefile && maple config $JOB_TREEDIR/Maplefile.simulation
cd $JOB_TREEDIR/outflow/buffer20 && rm -f Maplefile && maple config $JOB_TREEDIR/Maplefile.simulation
