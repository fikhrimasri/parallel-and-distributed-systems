# import library os
import os

# import library request
import requests

# import library threading
import threading

# import library urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.error, urllib.parse

# import library time
import time

#inisialisai url dengan alamat atau url dari file yang akan didownoad
url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg"

# fungsi untuk menghitung panjang data yang didownload
def buildRange(value, numsplits):
    # buat list untuk menampung hasil perhitungan 
    lst = []
    # lakukan perulangan sebanyak numsplits
    for i in range(numsplits):
        # ketika i=0 masukan hasil perhitungan kedalam list
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        # masukkan setiap hasil perhitungan yang didapatkan ke dalam list
        else:
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    return lst

# buat kelas SplitBufferThreads
class SplitBufferThreads(threading.Thread):
    """ Splits the buffer to ny number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """
     # fungsi __init__; init untuk assign url, byteRange dan hasil req = None
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        self.__url = url
        self.__byteRange = byteRange
        self.req = None

    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange})
    
    # fungsi untuk mendapatkan data
    def getFileData(self):
        return urllib.request.urlopen(self.req).read()

#fungsi utama
def main(url=None, splitBy=3):
    # ambil waktu awal menggunakan time.time()
    start_time = time.time()
    
    # cek apakah url valid atau tidak
    if not url:
        print("Please Enter some url to begin download.")
        return
    
    # mendapatkan nama file yang akan didownload dengan pemisah '/'
    fileName = url.split('/')[-1]
    
    # ambil ukuran file yang akan didownload 
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
    print("%s bytes to download." % sizeInBytes)
    
    # cek ukuran file valid atau tidak
    if not sizeInBytes:
        print("Size cannot be determined.")
        return
    
    # buat list untuk menampung hasil pengambilan data
    dataLst = []
    # lakukan perulangan sebanyak range splitBy
    for idx in range(splitBy):
        # menghitung panjang data yang didownload
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]
        
        # panggil thread untuk setiap url dan byteRange
        bufTh = SplitBufferThreads(url, byteRange)
        
        # jalankan thread
        bufTh.start()
        
        # tunggu hingga thread selesai
        bufTh.join()
        
        # masukkan setiap data yang didapatkan dalam list
        dataLst.append(bufTh.getFileData())

    # penggabungan data yang berada dalam list dataLst
    content = b''.join(dataLst)
    
#    cek dataLst ada atau tidak
    if dataLst:
        # cek apakah ada filename serupa jika ada hapus filename sebelumnya
        if os.path.exists(fileName):
            os.remove(fileName)
        # tampilkan lama waktu download
        print("--- %s seconds ---" % str(time.time() - start_time))
        # simpan file yang didownload sesuai isi variable filename
        with open(fileName, 'wb') as fh:
            fh.write(content)
        # tampikan hasilnya
        print("Finished Writing file %s" % fileName)

if __name__ == '__main__':
    main(url)

