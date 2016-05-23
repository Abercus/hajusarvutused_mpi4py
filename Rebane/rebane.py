# coding: utf-8
# rebane.py

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
