#!/bin/bash

# A script to install OpenMPI with Python bindings on Rocket
cd $HOME

module purge
module load python-2.7.3
module load openmpi-1.7.3
# Go Back to Home Directory then get and install Python MPI bindings
cd $HOME
export MPI4PYDIR=paralleelarvutused
mkdir $MPI4PYDIR
cd $MPI4PYDIR
wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-1.3.1.tar.gz
tar -xvf mpi4py-1.3.1.tar.gz
cd mpi4py-1.3.1
python setup.py build
python setup.py install --home=$HOME/$MPI4PYDIR/install
export PYTHONPATH=$HOME/$MPI4PYDIR/install/lib/python
