from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient #Import from AWS-IoT Library
import time#To create delay
from datetime import date, datetime #To get date and time
import Adafruit_DHT #Import DHT Library for sensor
import serial


myMQTTClient = AWSIoTMQTTClient("Voltage_Sensor")
myMQTTClient.configureEndpoint("a12aonicmmixym-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/aws/cert/CA.pem", "/home/pi/aws/cert/private.pem.key", "/home/pi/aws/cert/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

connecting_time = time.time() + 10

if time.time() < connecting_time:  #try connecting to AWS for 10 seconds
    myMQTTClient.connect()
    myMQTTClient.publish("topic/RPi__Voltage_Sensor", "connected", 0)
    print("MQTT Client connection success!")
else:
    print("Error: Check your AWS details in the program")


def voltagesensor():
  voltage = 0.0
  num_samples = 10
  sum = 0
  sample_count = 0
  ser=serial.Serial('/dev/ttyS0',115200)
  while (sample_count < num_samples):
       sum = sum + int(ser.readline().replace("\n",""))
       sample_count = sample_count + 1
  try:
     voltage = (float(sum)/float(num_samples)*4.75)/1023
     #print(voltage)
     voltage = voltage*4.95
     #print(voltage)
  except:
     print("Sensor down")
  #print ('{0:0.1f}'.format(voltage))
  return(voltage)

time.sleep(2) #wait for 2 secs

#Infinite Loop
now = datetime.now() #get date and time 
current_time = now.strftime('%Y-%m-%d %H:%M:%S') #get current time in string format 
    
voltage = voltagesensor()
#print(voltage)
#prepare the payload in string format 
#payload = '{ "timestamp": "' + current_time + '","temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ' }'
#payload = '{ "temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ',"timestamp": "' + current_time + '"}'
payload = '{ "voltage": '+str('{0:0.1f}'.format(voltagesensor()))+',"timestamp": "' + current_time + '"}'
print(payload) #print payload for reference 
myMQTTClient.publish("topic/RPi__Voltage_Sensor", payload, 0) #publish the payload
print("Published")
#time.sleep(1800) #Wait for 2 sec then update the values

