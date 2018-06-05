import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from time import sleep
import os
import requests

url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text="

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
#GPIO.setup(33, GPIO.IN)
pir=MotionSensor(13)

while True:
	#i=GPIO.input(13)
	#if i==0:
	#	#print "No Intruder"
	#	GPIO.output(35, 0)
	#	sleep(0.1)
	#if i==1:
	#	#print "Intruder Alert"
	#	GPIO.output(35,1)
	#	sleep(0.1)
	#pir.wait_for_motion()
	#GPIO.output(19,1)
	#pir.wait_for_no_motion()
	#GPIO.output(19, 0)
	with open("/home/pi/Projects/html/homeauto/check.txt") as f:
		motioncheck=f.read(1)
		#print ("file read"+motioncheck)
	if motioncheck=="1":
		#print "if condition"
		if pir.wait_for_motion():
			#print "motion detected"
			#GPIO.output(19,1)
			requests.get(url+'Motion Detected')
			sleep(5)
		#GPIO.output(19, 0)
		#requests.get(url+'Motion Detected')
		#pir.wait_for_no_motion()
		#requests.get(url+'Clear')
	sleep(1)