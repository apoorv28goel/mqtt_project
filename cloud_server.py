import paho.mqtt.client as mqtt
import time
import smtplib

broker_address = "iot.eclipse.org"
#broker_address = "192.168.1.206"

count = 0
count_warning = 5
humidity_warning_level = 80

def send_mail_alert():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("loging in")
    server.login("email.test.mqtt.alert@gmail.com", "1q2w3e4r%t")
    print("logged in")
    msg = "Warning: Humidty is more that 80% " 
    server.sendmail("email.test.mqtt.alert@gmail.com", "email.test.mqtt.alert@gmail.com", msg)
    print("exiting server")
    server.quit()



def humidity_check(msg):
        global count
        # msg = int(message.payload.decode("utf-8"))
        #print("msg :",msg)
        #print(msg)
        if msg >= humidity_warning_level:
            count = count +1
            #print("count:",count)

            if count >= count_warning:
                print("sending mail...")
                send_mail_alert()
                print("mail sent...")
                count = 0
        else:
            count = 0




def on_log(client, userdata, level, buf):
    print("log: "+buf)  


def on_message(client, userdata, message):
    time.sleep(1)
    msg = int(message.payload.decode("utf-8"))
    #print("recieved message = ",str(message.payload.decode("utf-8")))
    print(message.topic.split("/")[1]+" "+str(msg))

    
    #print(message.topic.split("/")[1])
    if message.topic.split("/")[1]== "humidity":
        humidity_check(msg)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        #print("connected flags = " + str(flags)+" result code "\
        #        +str(rc))
        cloud_server.subscribe("candy_factory/temp")
        cloud_server.subscribe("candy_factory/humidity")

        
    else:
        print("bad connection Returned Code ",rc)

def on_disconnect(client, userdata, flags, rc):
    print("Disconnected result code "+str(rc))

cloud_server = mqtt.Client("Cloud1")

cloud_server.on_message = on_message
cloud_server.on_connect =on_connect
#cloud_server.on_disconnect =on_disconnect
#cloud_server.on_log = on_log

cloud_server.connect(broker_address)
print("loop started")

#time.sleep(10)

#cloud_server.loop_stop()
cloud_server.loop_forever()


