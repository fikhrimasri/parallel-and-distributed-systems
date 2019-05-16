# import socket, sys, traceback dan threading
import socket
import sys
import traceback
from threading import Thread

# jalankan server
def main():
    start_server()

# fungsi saat server dijalankan
def start_server():
    # tentukan IP server
    host = "192.168.0.122"
    
    # tentukan port server
    port = 8888    

    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # option socket
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")

    # lakukan bind
    try:
        soc.bind((host, port))
    except:
        # exit pada saat error
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    # listen hingga 5 antrian
    soc.listen(5)
    print("Socket now listening")

    # infinite loop, jangan reset setiap ada request
    while True:
        # terima koneksi
        connection, address = soc.accept()
        
        # dapatkan IP dan port
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        # jalankan thread untuk setiap koneksi yang terhubung
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            # print kesalahan jika thread tidak berhasil dijalankan
            print("Thread did not start.")
            traceback.print_exc()

    # tutup socket
    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    # flag koneksi
    is_active = True

    # selama koneksi aktif
    while is_active:

        # terima pesan dari client
        client_input = connection.recv(max_buffer_size)
        
        # dapatkan ukuran pesan
        client_input_size = sys.getsizeof(client_input)
        
        # print jika pesan terlalu besar
        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}")

        # dapatkan pesan setelah didecode
        decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
        client_input = str(decoded_input)
        
        # jika "quit" maka flag koneksi = false, matikan koneksi
        if "quit" in client_input:
            # ubah flag
            is_active = False
            print("Client is requesting to quit")
            
            # matikan koneksi
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            
        else:
            # tampilkan pesan
            print("Processing the input received from " + ip +":" + port + " Message is: " + client_input)
            
# panggil fungsi utama
if __name__ == "__main__":
    main()