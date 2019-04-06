import RPi.GPIO as GPIO
import sys
import os
import requests
from time import sleep
import datetime
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
time =  datetime.datetime.now().strftime("%M")

def switchstatus():
	with open("/home/pi/Python_Scripts/homeauto/switch.txt") as f:
		temp=list(f)[-1]
		temp=temp.replace("\n","")
		global data
		data=json.loads(temp)

def switchoff():
	GPIO.output(16, 1)
	switchstatus()
	global data
	#data['light']='OFF'
	data['fan']='OFF'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	a="0"
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
		
def checkreset():
	check='0';
	with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

while True:
	hour =  int(datetime.datetime.now().strftime("%H"))
	while hour >4 and hour <9:
		hour =  int(datetime.datetime.now().strftime("%H"))
		time =  int(datetime.datetime.now().strftime("%H%M"))
		with open("/home/pi/Python_Scripts/homeauto/timer.txt") as timer:
			check=timer.read(1)
		if check=='1' and time ==500:
			switchoff()
			checkreset()
		if check=='2' and time ==530:
			switchoff()
			checkreset()
		if check=='3' and time ==600:
			switchoff()
			checkreset()
		if check=='4' and time ==630:
			switchoff()
			checkreset()
		if check=='5' and time ==700:
			switchoff()
			checkreset()
		if check=='6' and time ==830:
			switchoff()
			checkreset()
		if check=='7' and time ==900:
			switchoff()
			checkreset()
		sleep(60)
		#print time
	sleep(3600)
	#print hour
#print time
