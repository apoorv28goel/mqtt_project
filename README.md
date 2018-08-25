# mqtt_project
MQTT iot device and cloud server data exchange sample project

To run the project:
1.Run the cloud_server.py file then
2.Run the iot_device.py file(which sends the value of sensors)

Note:
To check the email alert capabilities the value of sensor is fixed to 100. you can comment that line for normal working and uncomment line number 15.

There are two sensors simulated in the iot_device file temperture and humidity.
Temperature values are send over the topic "candy_factory/temp" and humidity values are sent over topic "candy_factory/humidity"
Broker used is "iot.eclipse.org"

email_test.py was just to test email alert code.

Note: 
To see logs you can uncomment the line 53 in iot_device.py and 79 in cloud_server.py
