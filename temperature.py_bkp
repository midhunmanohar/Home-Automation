import sys
import RPi.GPIO as GPIO
import os
import requests
import Adafruit_DHT
from time import sleep
import datetime

url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text="


def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)
while True:
    while True:
       try:
          humidity, temperature = Adafruit_DHT.read_retry(11, 26)
          if temperature==None:
		     raise Exception("No readings")
	  break
       except:
          print("Sensor error... retrying...")
          sleep(10)
    #print(temperature,humidity)
    #print 'Temp: {0:0.1f}  Humidity: {1:0.1f}%'.format(temperature, humidity)
    #print temperature
    #print humidity
    #try:
    temp = '{0:0.1f}'.format(temperature)
    humi = '{0:0.1f}'.format(humidity)
    #except:
    #print("No value"+str(temperature)+", "+str(humidity))
    time =  datetime.datetime.now().strftime("%A, %d. %B %Y %H:%M")
    with open("/home/pi/Python_Scripts/homeauto/humidity.txt") as hum:
       humidity_prevalue=list(hum)[-1]
       humidity_prevalue=humidity_prevalue.replace("\n","")
    with open("/home/pi/Python_Scripts/homeauto/temperature.txt") as tem:
       temp_prevalue=list(tem)[-1]
       temp_prevalue=temp_prevalue.replace("\n","")
    with open("/home/pi/Python_Scripts/homeauto/temperature.txt","a") as tem:
       #print(temp)
       temp=int(float(temp))
       temp=str(temp)
       if temp != temp_prevalue and (temp[1]=="0" or temp[1]=="5"):
          while True:
             try:
                requests.get(url+'Temperature changed. Current Temperature: '+temp)
                break
             except:
                print("Connection error... retrying...")
                sleep(10)
       tem.write(temp +"\n")
       tem.flush()
       os.fsync(tem.fileno())
    with open("/home/pi/Python_Scripts/homeauto/humidity.txt","a") as hum:
       humi=int(float(humi))
       humi=str(humi)
       if humi != humidity_prevalue and (humi[1]=="0" or humi[1]=="5"):
          while True:
             try:
                requests.get(url+'Humidity changed. Current Humidity: '+humi)
                break
             except:
                print("Connection error... retrying...")
                sleep(10)
       hum.write(humi +"\n")
       hum.flush()
       os.fsync(hum.fileno())
    with open("/home/pi/Python_Scripts/homeauto/timestamp.txt","a") as tim:
       tim.write(time +"\n")
       tim.flush()
       os.fsync(tim.fileno())
    sleep(300)
