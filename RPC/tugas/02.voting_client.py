# import xmlrpc bagian client saja
import xmlrpc.client


# buat stub (proxy) untuk client
proxy = xmlrpc.client.ServerProxy("http://192.168.1.20:8000/RPC2")

print("vote:")
# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
proxy.vote_candidate("Muadz")
print("ahay")
# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
proxy.querry_result()

# lakukan pemanggilan fungsi lain terserah Anda