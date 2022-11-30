import paho.mqtt.client as mqtt
import urllib.request

MQTT_SERVER = "192.168.132.11"
MQTT_PATH = "sensors/ultrasonic"

#url ="http://172.16.6.138/IoT/data_insert.php?Customer_Name=Kwad&Place=Tema&Water_Level="

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    url ="http://192.168.132.241/iot/ultrasonic.php?DistanceCm="+str(float(msg.payload))
    contents = urllib.request.urlopen(url).read()
    print (float(msg.payload))

    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
