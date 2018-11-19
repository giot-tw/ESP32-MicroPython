# uplink every 10 secs
# OTAA mode
from machine import UART
import time
u = UART(1, baudrate=9600)
u.init(9600, bits=8, parity=None, stop=1)
print("Try To Connect")

# init G76S SiP
u.write("at+cmode=0\n")
time.sleep(2)
print(u.read().decode())
u.write("at+cappkey=11111111112222222222333333333344\n")
time.sleep(2)
print(u.read().decode())
u.write("at+cdeveui=0000000000000001\n")
time.sleep(2)
print(u.read().decode())
u.write("at+cappeui=1122334455667788\n")
time.sleep(2)
print(u.read().decode())
u.write("AT&W\n")
time.sleep(3)
print(u.read().decode())
u.write("ATZ\n")
time.sleep(2)
print(u.read().decode())
OTAA = False 
try:
    while True:
      if OTAA :
        u.write("at+dttx\n")
      time.sleep(3)
      print(time.time())
      data_list = u.read().splitlines()
      #print(u.read().splitlines())
      for i in data_list:
        print (i.decode())
        if i.decode() == "Over-the-Air Activation" :
          print ("OTAA Activated")
          OTAA = True
      time.sleep(7)
except Exception as error:
    print('An exception occurred: {}'.format(error))
    pass



