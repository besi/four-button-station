import secrets
import time
import ubinascii
from machine import ADC
from machine import Pin
from umqtt.robust import MQTTClient 

DELAY = 300

radio_a = Pin(4,Pin.IN)
radio_b = ADC(0)
radio_c = Pin(15,Pin.IN)
radio_d = Pin(13,Pin.IN)

Pin(16,Pin.OUT).value(0)
Pin(14,Pin.OUT,Pin.PULL_UP).value(0)
Pin(12,Pin.OUT,Pin.PULL_UP).value(0)
Pin(5,Pin.OUT,Pin.PULL_UP).value(0)


## MQTT
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = secrets.mqtt.topic
mqtt_server = secrets.mqtt.host
mqtt_port = secrets.mqtt.port
mqtt_user = secrets.mqtt.user
mqtt_password = secrets.mqtt.password

def connect():
  # if you set keepalive value - you have to send something to mqtt server to inform that you are alive in less time than keepalive value of seconds.
  client = MQTTClient(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_password,keepalive=DELAY * 2)
  client.set_last_will(topic_pub, '{ "status":"offline"} ', retain=False, qos=0)
  client.connect()
  print('Connected to %s MQTT broker' % mqtt_server)
  client.publish(topic_pub, bytes('{"status":"hello"}', 'utf-8'))
  return client

def stamp():
    (year,month,mday,h,m,s,weekday,yearday) = utime.localtime()
    return f"{hour}:{minute:02d}"
    
    
print(f"{stamp()} Starting up")
client = connect()

print("Connected to MQTT")
mqtt_keepalive = time.time()

while True:

    if time.time() - mqtt_keepalive > DELAY:
        mqtt_keepalive = time.time()
        print(f"{stamp()} Reconnecting MQTT...")
        client.reconnect()

    button = None
    if radio_a() == True: button = 'A'
    if radio_b.read()>500: button = 'B'
    if radio_c() == True: button = 'C'
    if radio_d() == True: button = 'D'
    
    if button != None:
        print(f"- {stamp()} {button} pressed >> MQTT")
        client.publish(topic_pub, bytes('{"button":"%s"}'% button, 'utf-8'))
        mqtt_keepalive = time.time()
        time.sleep(0.5)
    time.sleep(0.1)

