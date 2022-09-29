#!/bin/bash

#SBATCH --ntasks=5
#SBATCH -t 0-30:00

cd $SLURM_SUBMIT_DIR

module load openmpi-4.1.1

rm -f sim.par
cat ../../flash.par flash.par > sim.par

mpirun maple container run "/home/run/flashx_outflow -par_file sim.par"
