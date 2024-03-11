import machine
import time
rec1 = machine.Pin(2,machine.Pin.IN)
rec2 = machine.Pin(4,machine.Pin.IN)
rec3 = machine.Pin(9,machine.Pin.IN)
rec4 = machine.Pin(10,machine.Pin.IN)

rel1 = machine.Pin(16,machine.Pin.OUT)
rel2 = machine.Pin(14,machine.Pin.OUT)
rel3 = machine.Pin(12,machine.Pin.OUT)
rel4 = machine.Pin(5,machine.Pin.OUT)

while True:
    rel1.on()
    time.sleep(2)
    rel1.off()
    time.sleep(2)
    