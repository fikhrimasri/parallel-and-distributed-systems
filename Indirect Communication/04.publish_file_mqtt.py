# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address="localhost"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)


# print "baca file"
print ("read file")


# buka file surf.jpg
f = open("surf.jpg","rb")

# baca semua isi file
content = f.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
bytee = bytes(content)

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo",bytee)

# client loop mulai
client.loop()

# tutup file
f.close()
