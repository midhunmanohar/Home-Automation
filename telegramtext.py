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
import serial
ser=serial.Serial('/dev/ttyS0',115200)


bot = telepot.Bot('398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I')
url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text="


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
voltage = 0.0
sum = 0
sample_count = 0
num_samples = 10


def tempshow():
    with open("/home/pi/Projects/html/homeauto/temperature.txt") as tem:
       temp=list(tem)[-1]
    return(temp.replace("\n",""))
def humishow():
    with open("/home/pi/Projects/html/homeauto/humidity.txt") as hum:
       humi=list(hum)[-1]
    return(humi.replace("\n",""))
def timeshow():
    with open("/home/pi/Projects/html/homeauto/timestamp.txt") as tim:
       time=list(tim)[-1]
    return time
def switchstatus():
    with open("/home/pi/Projects/html/homeauto/switch.txt") as f:
		temp=list(f)[-1]
		temp=temp.replace("\n","")
		global data
		data=json.loads(temp)
def switchoff():
	GPIO.output(11, 1)
	GPIO.output(16, 1)
	switchstatus()
	global data
	data['light']='OFF'
	data['fan']='OFF'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	a="0"
	with open("/home/pi/Projects/html/homeauto/r1.light.txt","r+") as light:
		light.write(a)
		light.flush()
		os.fsync(light.fileno())
	with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
	with open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+") as fan:
		fan.write(a)
		fan.flush()
		os.fsync(fan.fileno())
	with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def voltagesensor():
   sum = 0
   sample_count = 0
   ser=serial.Serial('/dev/ttyS0',115200)
   while (sample_count < num_samples):
        sum = sum + int(ser.readline().replace("\n",""))
        sample_count = sample_count + 1
   try:
      voltage = (float(sum)/float(num_samples)*3.93)/1023
      #print(voltage)
      voltage = voltage*4.85
   except:
      print("Sensor down")
   #print ('{0:0.1f}'.format(voltage))
   return(voltage)

def handle(msg):
    global check
    #print ("handle start")
    chat_id = msg['chat']['id']
    command = msg['text']
    t= str(datetime.datetime.now().strftime("%-S"))

    if command=='/help':
       while True:
          try:
             bot.sendMessage(chat_id, text="Available commands: \n/start45\n/start53\n/temp\n/uptime\n/switchstatus\n/switchoff\n/stop\n/voltage")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)

    if command=='/start55':
       check="1"
       while True:
          try:
             bot.sendMessage(chat_id, text="CPU Temp Monitoring ON above 55")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 1")
       with open("/home/pi/Projects/html/homeauto/temp.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/start75':
       check="2"
       while True:
          try:
             bot.sendMessage(chat_id, text="CPU Temp Monitoring ON above 75")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 2")
       with open("/home/pi/Projects/html/homeauto/temp.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())
    if command=='/motiondetectorON':
       motioncheck="1"
       while True:
          try:
             bot.sendMessage(chat_id, text="Motion Detection ON")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 2")
       with open("/home/pi/Projects/html/homeauto/check.txt","w") as temp:
          temp.write(motioncheck +"\n")
          temp.flush()
          os.fsync(temp.fileno())
    if command=='/motiondetectorOFF':
       motioncheck="0"
       while True:
          try:
             bot.sendMessage(chat_id, text="Motion Detection OFF")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 2")
       with open("/home/pi/Projects/html/homeauto/check.txt","w") as temp:
          temp.write(motioncheck +"\n")
          temp.flush()
          os.fsync(temp.fileno())
    if command=='/switchoff':
	switchoff()
	while True:
          try:
             bot.sendMessage(chat_id, text="Room 1 Light & Fan OFF")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
    if command=='/switchstatus':
	 switchstatus()
	 while True:
          try:
             bot.sendMessage(chat_id, text="Switch Status\n\nRoom 1:\nLight: "+data["light"]+"\nFan: "+data["fan"]+"\nLast change: "+data["time"])
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
    if command=='/stop':
       check="0"
       while True:
          try:
             bot.sendMessage(chat_id, text="CPU Temp Monitoring OFF")
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
       #print ("check 0")
       with open("/home/pi/Projects/html/homeauto/temp.txt","w") as temp:
          temp.write(check +"\n")
          temp.flush()
          os.fsync(temp.fileno())

    if command=='/temp':
       while True:
          try:
             bot.sendMessage(chat_id, text="CPU Temp: "+getCPUtemperature())
             bot.sendMessage(chat_id, text="\n Room Temp: "+tempshow()+"C, Humidity: "+humishow()+"%\n\nLast update: "+timeshow())
             break
          except:
             print("No Internet, retrying...")
             sleep(10)
    if command=='/uptime':
       with open('/proc/uptime', 'r') as f:
          uptime_seconds = int(float(f.readline().split()[0]))
          uptime_string = str(timedelta(seconds = uptime_seconds))       
       while True:
          try:
             bot.sendMessage(chat_id, text="Uptime: "+uptime_string)
             break
          except:
             print("No Internet, retrying...")
             sleep(10)

    if command=='/voltage':
       while True:
         try:
           bot.sendMessage(chat_id, text="Reading battery voltage...")
           bot.sendMessage(chat_id, text="Battery Voltage: "+'{0:0.1f}'.format(voltagesensor()))
           break
         except:
           print("No Internet, retrying...")
           sleep(10)


#print ("main loop")
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    sleep(10)
