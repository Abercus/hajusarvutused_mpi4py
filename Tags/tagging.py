#!/usr/bin/env python
# coding: utf-8
# tagging.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
        lause1 = "Lause #1"
        lause2 = "Lause #2"
        comm.send(lause1, dest=1, tag=1)
        comm.send(lause2, dest=1, tag=2)
elif rank == 1:
        lause1 = comm.recv(source=0, tag=1)
        lause2 = comm.recv(source=0, tag=2)

        print lause1
        print lause2
