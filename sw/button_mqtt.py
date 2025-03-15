import secrets
import time
import ubinascii
import umqttsimple
from machine import ADC
from machine import Pin
from umqttsimple import MQTTClient 

DELAY = 5

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


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  machine.reset()


try:
  print("Connecting to MQTT...")
  client = connect()
except OSError as e:
  restart_and_reconnect()

print("Connected to MQTT")
while True:
  try:

    button = None
    if radio_a() == True: button = 'a'
    if radio_b.read()>500: button = 'b'
    if radio_c() == True: button = 'c'
    if radio_d() == True: button = 'd'

    if button != None:
        print(f"Button {button} pressed sending to MQTT")
        client.publish(topic_pub, bytes('{"button":"%s"}'% button, 'utf-8'))

        time.sleep(0.5)
    time.sleep(0.1)
  except OSError as e:
    restart_and_reconnect()
  except Exception as e:
      print("Erorr lost")

