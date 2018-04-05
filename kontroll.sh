#!/bin/bash

# Töö nimi on HelloWorld
#SBATCH -J HelloWorld
# See töö nõuab kahte arvutussõlme
#SBATCH -N 2
# Mitu tööülesannet sõlme kohta
#SBATCH --ntasks-per-node=2
# Kokku 4 protsessi.
# Väljundfail
#SBATCH --output=kontroll.out
# arvutusaeg
#SBATCH --time=00:10:00
# testime järjekorda
#SBATCH -p testing

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


