
import dht
import machine
#d = dht.DHT11(machine.Pin(4))
d = dht.DHT22(machine.Pin(4))

#d.measure()
#d.temperature()
#d.humidity()



import urequests
import time

while(True):
  d.measure()
  response = urequests.post("http://192.168.1.4:8080/dht", json={'temperature':d.temperature(),'humidity':d.humidity()})
  print(response.text)
  time.sleep(5)




