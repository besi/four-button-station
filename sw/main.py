import machine
import time
from machine import ADC

# Modified board. Radio b is connected to the ADC
radio_a = machine.Pin(4,machine.Pin.IN)
radio_b = ADC(0)
radio_c = machine.Pin(15,machine.Pin.IN)
radio_d = machine.Pin(13,machine.Pin.IN)

relay_1 = machine.Pin(16,machine.Pin.OUT)
relay_2 = machine.Pin(14,machine.Pin.OUT)
relay_3 = machine.Pin(12,machine.Pin.OUT)
relay_4 = machine.Pin(5,machine.Pin.OUT)


relay_1.off()
relay_2.off()
relay_3.off()
relay_4.off()

while True:
    if radio_a() == True: print("A pressed"); relay_1.value(1-relay_1.value()); time.sleep(0.5)
    if radio_b.read()>500: print("B pressed"); relay_2.value(1-relay_2.value()); time.sleep(0.5)
    if radio_c() == True: print("C pressed"); relay_3.value(1-relay_3.value()); time.sleep(0.5)
    if radio_d() == True: print("D pressed"); relay_4.value(1-relay_4.value()); time.sleep(0.5)

