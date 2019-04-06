from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient #Import from AWS-IoT Library
import time#To create delay
from datetime import date, datetime #To get date and time
import urllib

myMQTTClient = AWSIoTMQTTClient("RaspberryPI")
myMQTTClient.configureEndpoint("a12aonicmmixym-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/aws/cert/CA.pem", "/home/pi/aws/cert/private.pem.key", "/home/pi/aws/cert/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


connecting_time = time.time() + 10

if time.time() < connecting_time:  #try connecting to AWS for 10 seconds
    myMQTTClient.connect()
    myMQTTClient.publish("topic/rpi_price", "connected", 0)
    print("MQTT Client connection success!")
    print("topic/rpi_price")
else:
    print("Error: Check your AWS details in the program")


#time.sleep(2) #wait for 2 secs

now = datetime.now() #get date and time 
current_time = now.strftime('%Y-%m-%d') #get current time in string format 
pplink = "http://api.thingspeak.com/apps/thinghttp/send_request?api_key=30ADOFJF7240Y4OL"
dplink = "http://api.thingspeak.com/apps/thinghttp/send_request?api_key=X8HCUZMNZA6DDMBJ"
pp_read = urllib.urlopen(pplink)
dp_read = urllib.urlopen(dplink)
pp_data = pp_read.read()
dp_data = dp_read.read()
pp_data = pp_data.replace("b'","").replace("'","")
dp_data = dp_data.replace("b'","").replace("'","")
print(pp_data)
print(dp_data)
#prepare the payload in string format 
#payload = '{ "timestamp": "' + current_time + '","temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ' }'
payload = '{ "petrol": ' + str(pp_data) + ',"diesel": '+ str(dp_data) + ',"timestamp": "' + current_time + '"}'
print(payload) #print payload for reference 
myMQTTClient.publish("topic/rpi_price", payload, 0) #publish the payload
print("Published")
#time.sleep(3600) #Wait for 2 sec then update the values


