# chdir into directory containing the file
cd $JobTreeDir

cd $JobTreeDir/neumann && rm -f Maplefile && maple config $JobTreeDir/Maplefile.simulation
cd $JobTreeDir/outflow/buffer01 && rm -f Maplefile && maple config $JobTreeDir/Maplefile.simulation
cd $JobTreeDir/outflow/buffer10 && rm -f Maplefile && maple config $JobTreeDir/Maplefile.simulation
cd $JobTreeDir/outflow/buffer15 && rm -f Maplefile && maple config $JobTreeDir/Maplefile.simulation
cd $JobTreeDir/outflow/buffer20 && rm -f Maplefile && maple config $JobTreeDir/Maplefile.simulation
