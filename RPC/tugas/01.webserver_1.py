# import library socket karena akan digunakan request reply protocol sederhana
import socket

# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80
IPADDR = '192.168.1.35'
PORT = 80

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding 
s.bind((IPADDR,PORT))

# socket mendengarkan
s.listen(4)

# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"
print("Server berjalan dan melayani HTTP pada port ", PORT)

# loop forever
while True:
    # socket menerima koneksi
    print("menunggu koneksi")
    conn,addr = s.accept()

    # socket menerima data
    data = conn.recv(1024)

    # print data hasil koneksi
    print(data.decode())
    
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
    http_response = """\HTTP/1.1 200 OK

<html>
<head>
<title>Web Server Sederhana</title>
</head>
<body>

<h1>Heading 1</h1>
<p>Ini adalah contoh paragraf.</p>
<img src="https://www.surfertoday.com/images/stories/surfetiquette.jpg">

</body>
</html>
"""
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8 
    conn.sendall(http_response.encode("utf-8"))
    
    # tutup koneksi
    conn.close()

# Selamat! Kamu telah berhasil membuat web server sederhana. 