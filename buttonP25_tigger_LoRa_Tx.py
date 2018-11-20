from machine import Pin
sw = Pin(25,Pin.IN)
led = Pin(2,Pin.OUT)
while True:
  val = sw.value()
  led.value(val)
  print(val)

