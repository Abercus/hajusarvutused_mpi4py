#!/bin/bash

# T�� nimi on HelloWorld
#SBATCH -J HelloWorld
# See t�� n�uab kahte arvutuss�lme
#SBATCH -N 2
# Mitu t���lesannet s�lme kohta
#SBATCH --ntasks-per-node=2
# Kokku 4 protsessi.
# V�ljundfail
#SBATCH --output=kontroll.out

# Vajalike moodulite laadimine.
module purge
module load openmpi-1.7.3
module load python-2.7.3

# Kausta nimi
export MPI4PYDIR=paralleelarvutused

# Pythoni wrapperi asukoht
export PYTHONPATH=$HOME/$MPI4PYDIR/install/lib/python

# Jooksutame kasutades mpi'd.
mpirun python helloWorld/helloworld.py
