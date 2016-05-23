#!/usr/bin/env python
# coding: utf-8
# helloworld.py

# Importime vajaliku mpi4py teegi.
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank % 2 == 0:
	print "Tere, Maailm! Protsessi nr: %d \n" % (rank)
else:
	print "Head aega, Maailm! Protsessi nr: %d \n" % (rank) 
