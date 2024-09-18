import paho.mqtt.client as mqtt

#CREATING A SUBSCRIBER
def on_message(client, userdata, message):
    print(f"MESSAGE RECEIVED: {message.payload.decode()} in the topic {message.topic}")

    #connecting to the broker
broker_adress = "test.mosquitto.org"
broker_port = 1883
client = mqtt.Client("SUBSCRIBER")
print("CONNECTING TO THE BROKER...")
client.connect(broker_adress, broker_port)

    #subscribing to the topic
client.subscribe("home/room/temperature")
print("SUBSCRIBED TO THE TOPIC")
client.on_message = on_message

    #keeping alive
client.loop_forever()
