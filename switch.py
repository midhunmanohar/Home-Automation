import RPi.GPIO as GPIO
import os
import json
import datetime
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(11, 0)
GPIO.output(16, 0)
a="0"
b="1"
switch = {'light':'', 'fan':'','time':''}

def switchstatus():
	with open("/home/pi/Projects/html/homeauto/switch.txt") as f:
		temp=list(f)[-1]
		temp=temp.replace("\n","")
		global switch
		switch=json.loads(temp)

try:
	switchstatus()
	while True:
		input1=GPIO.input(40)
		input2=GPIO.input(38)
		with open("/home/pi/Projects/html/homeauto/r1.light.txt", "r+") as light:
      			Lstate=light.read(1)
		with open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+") as fan:
			Fstate=fan.read(1)
		if input1 == 0:
			if Lstate=="0":
				#print ("Switch OFF Light")
				GPIO.output(11, 0)
				switch['light']='ON'
				switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
				with open("/home/pi/Projects/html/homeauto/r1.light.txt","r+") as light:
					light.write(b)
					light.flush()
					os.fsync(light.fileno())
				with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		            		json.dump(switch,f)
		            		f.write("\n")

			if Lstate=="1":
				#print ("Switch ON Light")
				GPIO.output(11, 1)
				switch['light']='OFF'
				switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
				with open("/home/pi/Projects/html/homeauto/r1.light.txt","r+") as light:
					light.write(a)
					light.flush()
					os.fsync(light.fileno())
				with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		            		json.dump(switch,f)
		            		f.write("\n")
		if input2 == 0:
			if Fstate=="0":
				#print ("Switch OFF Fan")
				GPIO.output(16, 0)
				switch['fan']='ON'
				switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
				with open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+") as fan:
					fan.write(b)
					fan.flush()
					os.fsync(fan.fileno())
				with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		            		json.dump(switch,f)
		            		f.write("\n")

			if Fstate=="1":
				#print ("Switch ON Fan")
				GPIO.output(16, 1)
				switch['fan']='OFF'
				switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
				with open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+") as fan:
					fan.write(a)
					fan.flush()
					os.fsync(fan.fileno())
				with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		            		json.dump(switch,f)
		            		f.write("\n")


		sleep(0.2)
finally:
	GPIO.cleanup()
