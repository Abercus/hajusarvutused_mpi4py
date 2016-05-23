 #!/usr/bin/env python
# coding: utf-8
# helloworld.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
# Kõigil protsessidel väljaarvatud järjekorranumbriga 0 andmed puuduvad.

data = None
if rank == 0:
	data = [1,2,3,4,5,6,7,8,9,10]
# Broadcastiga
comm.bcast(data, root=0)

print data

"""
# Broadcastita
if rank == 0:
	data = 1
	for i in range(1, size):
		comm.send(data, dest=i, tag=1)
else:
	data = comm.recv(source=0, tag=1)

comm.Barrier()
print data, "protsessilt", rank
"""
