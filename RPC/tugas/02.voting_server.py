# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

# Buat server
with SimpleXMLRPCServer(('192.168.1.35', 8000)) as server:
	server.register_introspection_functions()

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
	pemilu = {'nama':["narto","jokowo","prawowo","al"], 'vote':[0,0,0,0]}
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
	lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
	def vote_candidate(x):
        # critical section dimulai harus dilock
		lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
		if x in pemilu['nama']:
			idx = pemilu['nama'].index(x)
			pemilu['vote'][idx]+=1
		print(pemilu['vote'])
		
        # critical section berakhir, harus diunlock
		lock.release()
		return "YASH"
    # register fungsi vote_candidate() sebagai vote
	server.register_function(vote_candidate)
	
    # buat fungsi bernama querry_result
	def querry_result():
        # critical section dimulai
		lock.acquire()
        # hitung total vote yang ada
		totalvote = sum(pemilu['vote'])
        # hitung hasil persentase masing-masing kandidat
		for i in range(len(pemilu['nama'])):
			persentase = (pemilu['vote'][i]/totalvote)*100
			print("Nama : ", pemilu['nama'][i])
			print("Persentase : ", persentase, "%")
				
		# critical section berakhir
		lock.release()
		return "YASH"
		
	# register querry_result sebagai querry
	server.register_function(querry_result, 'querry_result')
	
	print ("Server voting berjalan...")
    # Jalankan server
	server.serve_forever()
