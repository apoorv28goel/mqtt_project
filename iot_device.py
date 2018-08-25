import paho.mqtt.client as mqtt
import time
import random

#configrable parameters
broker_address = "iot.eclipse.org"
#broker_address = "192.168.1.206"
range_temp = [200,300]
range_humidity = [0,100]
interval = 1

#simutated sensor to send random values 
def sensor(range_sensor):    
    # time.sleep(interval)
    #value = random.randint(range_sensor[0],range_sensor[1])
    #to test the waring email uncomment the following lines lines
    value = 100
    return value





def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_message(client, userdata, message):
    time.sleep(1)
    print("recieved message = ",str(message.payload.decode("utf-8")))
    print("message topic = ",message.topic)
    print("message qos = ",message.qos)
    message
    print("message retain flag = ", message.retain)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected flags = " + str(flags)+" result code "\
                +str(rc))
    else:
        print("bad connection Returned Code ",rc)

#def on_publish()

def on_disconnect(client, userdata, flags, rc):
    print("Disconnected result code "+str(rc))


iot_device = mqtt.Client("Device1")

iot_device.on_message = on_message
iot_device.on_connect = on_connect
iot_device.on_disconnect = on_disconnect
#iot_device._on_log = on_log

iot_device.connect(broker_address)
iot_device.loop_start()

for i in range(10):
    #print(i)
    temp = sensor(range_temp)
    humidity = sensor(range_humidity)
    print("temp:",temp)
    print("humidity:",humidity)


    iot_device.publish("candy_factory/temp",temp)
    iot_device.publish("candy_factory/humidity",humidity)

    time.sleep(interval)
    

iot_device.loop_stop()