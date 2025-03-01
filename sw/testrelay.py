import machine
import time
radio_b = machine.Pin(2,machine.Pin.IN)
radio_a = machine.Pin(4,machine.Pin.IN)
radio_c = machine.Pin(15,machine.Pin.IN)
radio_d = machine.Pin(13,machine.Pin.IN)

# rec3 = machine.Pin(9,machine.Pin.IN) # Fails
# rec4 = machine.Pin(10,machine.Pin.IN) # Fails

relay_1 = machine.Pin(16,machine.Pin.OUT)
relay_2 = machine.Pin(14,machine.Pin.OUT)
relay_3 = machine.Pin(12,machine.Pin.OUT)
relay_4 = machine.Pin(5,machine.Pin.OUT)

while True:
    relay_1.on()
    relay_2.on()
    relay_3.on()
    relay_4.on()

    time.sleep(2)
    relay_1.off()
    relay_2.off()
    relay_3.off()
    relay_4.off()
    time.sleep(2)
