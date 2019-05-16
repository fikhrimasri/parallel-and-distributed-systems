# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
s = xmlrpc.client.ServerProxy('http://192.168.1.20:1059')

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    binary_data=xmlrpc.client.Binary(handle.read())
s.file_upload(binary_data)

# panggil fungsi untuk upload yang ada di server
print(s.file_upload(binary_data))
