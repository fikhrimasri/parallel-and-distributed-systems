# import socket dan sys
import socket
import sys

# fungsi utama
def main():
    # buat socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # tentukan IP server target
    host = "192.168.0.122"
    
    # tentukan por server
    port = 8888

    # lakukan koneksi ke server
    try:
        soc.connect((host, port))
    except:
        # print error
        print("Connection error")
        # exit
        sys.exit()
    
    # tampilkan menu, enter quit to exit
    print("Enter 'quit' to exit")
    message = input(" -> ")

    # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
        soc.sendall(message.encode("utf8"))
        
        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    soc.send(b'--quit--')

# panggil fungsi utama
if __name__ == "__main__":
    main()