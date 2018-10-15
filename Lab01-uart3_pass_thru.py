# i/o A15 switches boot modes from dupterm to UART6 <> UART3 pass through for screen programming.

import pyb
from pyb import UART
import uos

sp = pyb.Pin('A15', pyb.Pin.IN)  # Activate input A15 (red led) connected to ESP8266 i/o 14 
pyb.delay(10)

if sp.value() == 1:
	uart6 = UART(6)
	uart6.init(115200, read_buf_len = 256)
	uart3 = UART(3)                         
	uart3.init(115200, read_buf_len = 256)  # Try higher values if necessary

	while True:
		nrx = uart3.any()  # Count available characters
		if nrx:
			uart6.write(uart3.read(nrx))  # Only read what's available: it should never time out

		nrx = uart6.any()
		if nrx:
			uart3.write(uart6.read(nrx))
	
else:
	uart6 = UART(6)
	uart6.init(115200)
	uos.dupterm(uart6)  # duplicate repl on UART(6)

	pyb.main('main.py') # main script to run after this one

	pyb.usb_mode('CDC') # act as a serial (CDC) and not a storage device (MSC)
