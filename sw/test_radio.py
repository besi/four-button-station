import machine
import time
radio_b = machine.Pin(2,machine.Pin.IN)
radio_a = machine.Pin(4,machine.Pin.IN)
radio_c = machine.Pin(15,machine.Pin.IN)
radio_d = machine.Pin(13,machine.Pin.IN)

while True:
    if radio_a() == True: print("A pressed"); time.sleep(0.5)
    if radio_b() == True: print("B pressed"); time.sleep(0.5)
    if radio_c() == True: print("C pressed"); time.sleep(0.5)
    if radio_d() == True: print("D pressed"); time.sleep(0.5)
