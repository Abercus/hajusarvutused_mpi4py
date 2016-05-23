# coding: utf-8
# tagging.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	# Loome massiivid
	massiiv1 = [i for i in range(size*2)]
	massiiv2 = [i+1 for i in range(size*2)]
	# Arvutab osa suuruse
	osaSuurus = len(massiiv1)/size
	# Saadab töö laiali. Iga protsess saab len(massiiv)/size, ehk praegu 2 elementi.
	for i in range(1, size):
		comm.send(massiiv1[i*osaSuurus:(i*2)*osaSuurus], dest=i, tag=1)
		comm.send(massiiv2[i*osaSuurus:(i*2)*osaSuurus], dest=i, tag=2)
	
	# Protsess teeb oma töö.
	osa1 = massiiv1[:osaSuurus]
	osa2 = massiiv2[:osaSuurus]
	tulemus = []
	for i in range(len(osa1)):
		tulemus.append(float(osa1[i])/osa2[i])
		
	# Küsime teistelt töö tagasi.
	for i in range(1, size):
		tulemus = tulemus + comm.recv(source=i, tag=3)
		
	print tulemus

else:
	# Tagidega kindlustame, et osa1 on massiiv1'st ja osa2 on massiiv2'st
	osa1 = comm.recv(source=0, tag=1)
	osa2 = comm.recv(source=0, tag=2)
	tulemus = []
	for i in range(len(osa1)):
		tulemus.append(float(osa1[i])/osa2[i])
	
	# Saadame tehtud töö tagasi algprotsessile
	comm.send(tulemus, dest=0, tag=3)
	
