# chdir into directory containing the file
cd $JOB_FILE_HOME

cd $JOB_FILE_HOME/neumann && rm -f Maplefile && maple config $JOB_FILE_HOME/Maplefile.simulation
cd $JOB_FILE_HOME/outflow/buffer01 && rm -f Maplefile && maple config $JOB_FILE_HOME/Maplefile.simulation
cd $JOB_FILE_HOME/outflow/buffer10 && rm -f Maplefile && maple config $JOB_FILE_HOME/Maplefile.simulation
cd $JOB_FILE_HOME/outflow/buffer15 && rm -f Maplefile && maple config $JOB_FILE_HOME/Maplefile.simulation
cd $JOB_FILE_HOME/outflow/buffer20 && rm -f Maplefile && maple config $JOB_FILE_HOME/Maplefile.simulation
