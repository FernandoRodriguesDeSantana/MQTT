import paho.mqtt.client as mqtt

#CREATING A PUBLISHER

    #connecting to the broker
broker_adress = "test.mosquitto.org"
broker_port = 1883
client = mqtt.Client("PUBLISHER")
client.connect(broker_adress, broker_port)

    #publishing a message
client.publish("home/room/temperature", "22.5")
print("MESSAGE PUBLISHED")
