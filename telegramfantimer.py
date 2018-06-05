import sys
import requests
from time import sleep
from datetime import timedelta
import random
import datetime
import telepot
import os
import json
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO

bot = telepot.Bot('460125361:AAEZ8CZWEGJ6C8Gu0REBiBubCJxALeYUFHk')
url = "https://api.telegram.org/bot460125361:AAEZ8CZWEGJ6C8Gu0REBiBubCJxALeYUFHk/sendMessage?chat_id=395386694&text="


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)


def switchstatus():
    with open("/home/pi/Projects/html/homeauto/switch.txt") as f:
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
	with open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+") as fan:
		fan.write(a)
		fan.flush()
		os.fsync(fan.fileno())
	with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")

def handle(msg):
    global check
    #print ("handle start")
    chat_id = msg['chat']['id']
    command = msg['text']
    t= str(datetime.datetime.now().strftime("%-S"))

    if command=='/help':
       while True:
          try:
             bot.sendMessage(chat_id, text="Available commands: \n/set0430\n/set0500\n/set0530\n/set0600\n/set0830\n/clear\n")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)

    if command=='/set0430':
       check="1"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 04:30AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0500':
       check="2"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 05:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())
 
    if command=='/set0530':
       check="3"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 05:30AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0600':
       check="4"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 06:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())
	
    if command=='/set0830':
       check="5"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 08:30AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/clear':
       check="0"
       while True:
          try:
             bot.sendMessage(chat_id, text="Timer cleared")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())


#print ("main loop")
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    sleep(10)
