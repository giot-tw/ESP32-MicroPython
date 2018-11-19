
# i/o A15 switches boot modes from dupterm to UART6 <> UART3 pass through for screen programming.

import pyb
from pyb import UART
import uos

#sp = pyb.Pin('A15', pyb.Pin.IN)  # Activate input A15 (red led) connected to ESP8266 i/o 14 
pyb.delay(10)

if sp.value() == 1:
	uart0 = UART(0)
	uart0.init(115200, read_buf_len = 256)
	uart1 = UART(1)                         
	uart1.init(9600, read_buf_len = 256)  # Try higher values if necessary

	while True:
		nrx = uart1.any()  # Count available characters
		if nrx:
			uart0.write(uart1.read(nrx))  # Only read what's available: it should never time out

		nrx = uart0.any()
		if nrx:
			uart1.write(uart0.read(nrx))
	
else:
	uart0 = UART(0)
	uart0.init(115200)
	uos.dupterm(uart0)  # duplicate repl on UART(6)

	pyb.main('main.py') # main script to run after this one

	pyb.usb_mode('CDC') # act as a serial (CDC) and not a storage device (MSC)


