#!/usr/bin/env python
# coding: utf-8
# tsykkel.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

number = 5

if rank == 0:
        print number, rank
        comm.send(number + 1, dest=rank+1)
        number = comm.recv(source=size-1)
	print number, rank
else:

        number = comm.recv(source=rank-1)
        print number, rank
        comm.send(number + 1, dest=(rank+1)%size)
