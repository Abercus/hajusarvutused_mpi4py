# coding: utf-8
# rebane2.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
        data = "Mida rebane ütleb?"
        comm.send(data, dest=1)
        print data, rank
elif rank == 1:
        data = comm.recv(source = 0)
        print data, rank
        if size > 2:
                comm.send(data, dest = 2)
elif size > 2 and rank == 2:
        data = comm.recv(source = 1)
        print data, rank
