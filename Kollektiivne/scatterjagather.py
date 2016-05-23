#!/usr/bin/env python
# coding: utf-8
# helloworld.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Kõigil protsessidel väljaarvatud järjekorranumbriga 0 andmed puuduvad.
data = None
# Loome protsessil järjekorranumbriga 0 massiivi, mis on pikkusega size (ehk protsesside arv)
if rank == 0:
	data = [i*2 for i in range(size)]
	print "algsed andmed", data
data = comm.scatter(data, root=0)

# Lahutame k6igil protsessidel saadud andmetest maha 1
data = data - 1
# Saadame töödeldud andmed tagasi. Protsess 0 saab endale töödeldud andmed.
data = comm.gather(data, root=0)
if rank == 0:
	print "lõplikud andmed", data
