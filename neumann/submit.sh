#!/bin/bash

#SBATCH --ntasks=4
#SBATCH -t 0-30:00

cd $SLURM_SUBMIT_DIR

module load openmpi-4.1.1

mpirun maple container run "/home/run/flashx_neumann"
