#!/usr/bin/env python
# coding: utf-8
# scatterjagather2.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Kõigil protsessidel väljaarvatud järjekorranumbriga 0 andmed puuduvad.
data = None
# Loome protsessil järjekorranumbriga 0 massiivi, mis on pikkusega size (ehk protsesside arv)
if rank == 0:
        algAndmed = [i*2 for i in range(size*2)]
        data = []
        for i in range(0, len(algAndmed), 2):
                data.append([algAndmed[i]]+[algAndmed[i+1]])
        print "algsed andmed", algAndmed
data = comm.scatter(data, root=0)
# Lahutame k6igil protsessidel saadud andmetest maha 1
for i in range(len(data)):
        data[i] = data[i] - 1
# Saadame töödeldud andmed tagasi. Protsess 0 saab endale töödeldud andmed.
data = comm.gather(data, root=0)

if rank == 0:
        tulemus = [y for x in data for y in x]
        print "lõplikud andmed", tulemus
