from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient #Import from AWS-IoT Library
import time#To create delay
from datetime import date, datetime #To get date and time
import Adafruit_DHT #Import DHT Library for sensor


myMQTTClient = AWSIoTMQTTClient("thing/Temp_Sensor_RaspberryPI")
myMQTTClient.configureEndpoint("a12aonicmmixym-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/aws/cert/CA.pem", "/home/pi/aws/cert/private.pem.key", "/home/pi/aws/cert/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

sensor_name = Adafruit_DHT.DHT11 #we are using the DHT11 sensor
sensor_pin = 26 

connecting_time = time.time() + 10

if time.time() < connecting_time:  #try connecting to AWS for 10 seconds
    myMQTTClient.connect()
    myMQTTClient.publish("topic/RPi_Sensor", "connected", 0)
    print("MQTT Client connection success!")
else:
    print("Error: Check your AWS details in the program")


time.sleep(2) #wait for 2 secs

#Infinite Loop
now = datetime.now() #get date and time 
current_time = now.strftime('%Y-%m-%d %H:%M:%S') #get current time in string format 
    
humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin) #read from sensor and save respective values in temperature and humidity varibale  
time.sleep(2) #Wait for 2 sec then update the values
#prepare the payload in string format 
#payload = '{ "timestamp": "' + current_time + '","temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ' }'
payload = '{ "temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ',"timestamp": "' + current_time + '"}'
print(payload) #print payload for reference 
myMQTTClient.publish("topic/RPi_Sensor", payload, 0) #publish the payload
print("Published")
#time.sleep(3600) #Wait for 2 sec then update the values
