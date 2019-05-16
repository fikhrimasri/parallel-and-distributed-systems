# import os, re dan threading
import threading,re,os
from threading import Thread
# import time
import time

# buat kelas ip_check
class ip_check(threading.Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1
        
    
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        pingaling = os.popen("ping -n 2"+self.ip,"r")
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            line = pingaling.readline()
            
            # break jika tidak ada line lagi
            if not line: break
            
            # baca hasil per line dan temukan pola Received = x
            received = re.findall(ip_check.lifeline,line)
            
            # tampilkan hasilnya
            if received:
                self.status = int(received[0])
                
    # fungsi untuk mengetahui status; 
    # 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        # 0 = tidak ada respon
        if self == 0:
            return "tidak ada respon"
        # 1 = ada loss
        elif self == 1:
            return "hidup tapi ada loss"
        # 2 = hidup
        elif self == 2:
            return "hidup"
        # -1 = seharusnya tidak terjadi
        else:
            return "seharusnya tidak terjadi"
        
status = ("tidak ada respon","hidup tetapi ada yang hilang","hidup")
# buat regex untuk mengetahui isi dari r"Received = (\d)"
ip_check.lifeline = re.compile(r"Received = (\d)")

# catat waktu awal
print(time.ctime())
start = time.time()

# buat list untuk menampung hasil pengecekan
pinglist = []

# lakukan ping untuk 20 host
for suffix in range(1,20):
    # tentukan IP host apa saja yang akan di ping
    ip = "10.30.32."+str(suffix)
    
    # panggil thread untuk setiap IP
    current = ip_check(ip)
    
    # masukkan setiap IP dalam list
    pinglist.append(current)
    
    # jalankan thread
    current.start()

# untuk setiap IP yang ada di list
for el in pinglist:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    print(("Status dari "+ el.ip + " adalah " + status[el.status]))    

# catat waktu berakhir
print(time.ctime())
end = time.time()

# tampilkan selisih waktu akhir dan awal
print("selisih waktu akhir dan awal :",end-start)