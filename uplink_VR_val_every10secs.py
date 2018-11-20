
import time
from machine import Pin
from machine import UART
P25 = Pin(25,Pin.IN)
led = Pin(2,Pin.OUT)
u = UART(1, baudrate=9600)
u.init(9600, bits=8, parity=None, stop=1)
print("Try To Connect LoRa Module....")

try:
    while True:
      u.write("AT+DTTX\n")
      time.sleep(3)
      print("timestamp:" + str(time.time()))
      data_list = u.read().splitlines()
      for i in data_list:
        if i:
          print (i.decode())
          #print (i)
      while P25.value():
        time.sleep(1)
        print("wait for tigger ...")
        print(time.time())
      print("P25 is tigger")
except Exception as error:
    print('An exception occurred: {}'.format(error))
    pass
