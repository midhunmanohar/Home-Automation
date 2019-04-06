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
	with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")

def handle(msg):
    global check
    #print ("handle start")
    chat_id = msg['chat']['id']
    command = msg['text']
    t= str(datetime.datetime.now().strftime("%-S"))
    print (command)
    if command=='/help@g6home_bot':
       while True:
          try:
             bot.sendMessage(chat_id, text="Available commands: \n/set0500\n/set0530\n/set0600\n/set0630\n/set0700\n/set0830\n/set0900\n/clear\n")
             print ("Available commands: \n/set0500\n/set0530\n/set0600\n/set0630\n/set0700\n/set0830\n/set0900\n/clear\n")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)

    if command=='/set0500@g6home_bot':
       check="1"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 05:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0530@g6home_bot':
       check="2"
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
 
    if command=='/set0600@g6home_bot':
       check="3"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 06:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0630@g6home_bot':
       check="4"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 06:30AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())
	
    if command=='/set0700@g6home_bot':
       check="5"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 07:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0830@g6home_bot':
       check="6"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 08:30AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/set0900@g6home_bot':
       check="7"
       while True:
          try:
             bot.sendMessage(chat_id, text="Fan will switch OFF at 09:00AM")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())
		  
    if command=='/clear@g6home_bot':
       check="0"
       while True:
          try:
             bot.sendMessage(chat_id, text="Timer cleared")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Python_Scripts/homeauto/timer.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())


#print ("main loop")
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    sleep(10)
