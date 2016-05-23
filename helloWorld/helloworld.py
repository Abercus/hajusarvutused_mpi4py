#!/usr/bin/env python
# coding: utf-8
# helloworld.py

# Impordime vajaliku mpi4py teegi.
from mpi4py import MPI

# Kommunikaatori küsimine
comm = MPI.COMM_WORLD

# Küsime muutujasse size kogu protsesside arvu.
size = comm.Get_size()
# Küsime muutujasse nimega rank, et mitmes protsess on. Loendamine algab 0st
rank = comm.Get_rank()
# Küsime nime.
name = MPI.Get_processor_name()

# Trükime väljundi.
print "Tere, Maailm! Protsessi nr: %d kokku protsesse: %d nimega %s.\n" % (rank, size, name)
