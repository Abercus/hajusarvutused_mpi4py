 #!/usr/bin/env python
# coding: utf-8
# barrier.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print rank, size
comm.Barrier()
print rank, size

	
	