#!/bin/bash
#SBATCH -J tsykkel
#SBATCH -n 20
#SBATCH --time=00:10:00
#SBATCH -p testing

module purge
module load openmpi-1.7.3
module load python-2.7.3
export MPI4PYDIR=paralleelarvutused
export PYTHONPATH=$HOME/$MPI4PYDIR/install/lib/python

mpirun python tsykkel.py
