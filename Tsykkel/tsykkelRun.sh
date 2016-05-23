#!/bin/bash
#SBATCH -J tsykkel
#SBATCH -n 20

module purge
module load openmpi-1.7.3
module load python-2.7.3
export MPI4PYDIR=paralleelarvutused
export PYTHONPATH=$HOME/$MPI4PYDIR/install/lib/python

mpirun python tsykkel.py
