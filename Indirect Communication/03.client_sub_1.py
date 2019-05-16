# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# import re (regular expression) untuk filter
import re

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # filter pesan yang masuk 
#    print("message received ", str(message.payload.decode("utf-8")))
    pesan = str(message.payload.decode("utf-8")) + "\n"
    match = re.match("AAA",pesan)
    print(match)
    #jika ada pola AAA tulis ke result_a.txt
    if match:
        f = open("result_a.txt", "at")
        f.write(pesan)
        f.close()   
    # lainnya tulis ke result_b.txt
    else:
        f = open("result_b.txt", "at")
        f.write(pesan)
        f.close()
    
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address="192.168.3.10"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port = 1883)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")
client.subscribe([("topik 1",1),("topik 2",2)])

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()
