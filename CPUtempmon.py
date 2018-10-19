from time import sleep
import os
import requests
import RPi.GPIO as GPIO

url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text="

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
counter = 0

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

while 1:
   with open("/home/pi/Python_Scripts/homeauto/temp.txt") as tempv:
      tempval=tempv.read(1)
      cputemp= int(float(getCPUtemperature()))
      if (tempval=="1" or tempval=="2") and cputemp<40:
          GPIO.output(18, False)
          if (counter == 1):
             try:
                requests.get(url+'CPU Fan OFF')
	        counter = 0
             except:
                print("Connection error... retrying...")
      if (tempval=="1" or tempval=="2") and cputemp>41:
 	  GPIO.output(18, True)
	  if (counter == 0):
	     try:
                requests.get(url+'CPU Fan ON')
		print(counter)
		counter = 1
             except:
                print("Connection error... retrying...")
      if tempval=="1" and cputemp>55:
         while True:
            try:
               requests.get(url+'CPU Temp High '+getCPUtemperature())
               break
            except:
               print("Connection error... retrying...")
               sleep(10)
      if tempval=="2" and cputemp>75:
         while True:
            try:
               requests.get(url+'CPU Temp High '+getCPUtemperature())
               break
            except:
               print("Connection error... retrying...")
               sleep(10)
      if cputemp>85:
         while True:
            try:
               requests.get(url+'CPU Temp CRITICAL '+getCPUtemperature())
               break
            except:
               print("Connection error... retrying...")
               sleep(10)	  
   sleep(30)
