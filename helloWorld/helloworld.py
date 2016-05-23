#!/usr/bin/env python
# coding: utf-8
# helloworld.py

# Impordime vajaliku mpi4py teegi.
from mpi4py import MPI

# Kommunikaatori k�simine
comm = MPI.COMM_WORLD

# K�sime muutujasse size kogu protsesside arvu.
size = comm.Get_size()
# K�sime muutujasse nimega rank, et mitmes protsess on. Loendamine algab 0st
rank = comm.Get_rank()
# K�sime nime.
name = MPI.Get_processor_name()

# Tr�kime v�ljundi.
print "Tere, Maailm! Protsessi nr: %d kokku protsesse: %d nimega %s.\n" % (rank, size, name)
