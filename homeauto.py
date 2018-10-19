import RPi.GPIO as GPIO
import time, datetime
from time import sleep
from flask import Flask, render_template
import shelve
import os
import json
from Adafruit_IO import *

app = Flask(__name__)
app.url_map.strict_slashes = False

AIO_KEY = '1843a8e537fe47a98d6e0907e8001d6f'
aio = Client('midhunmanohar',AIO_KEY)



a="0"
b="1"
global lstatus, fstatus
#lstatus=""
#fstatus=""
switch = {'light':'', 'fan':'', 'time':''}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))


def room1lightON():
	GPIO.output(11,False)
	global lstatus
	lstatus="ON"
	switch['light']='ON'
	switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(switch,f)
		f.write("\n")
	# with open("/home/pi/Python_Scripts/homeauto/r1.light.txt","w") as light:
		# light.write(b)
		# light.flush()
		# os.fsync(light.fileno())
	sleep(1)

def room1lightOFF():
	GPIO.output(11,True)
	global lstatus
	lstatus="OFF"
	switch['light']='OFF'
	switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(switch,f)
		f.write("\n")
	# with open("/home/pi/Python_Scripts/homeauto/r1.light.txt","w") as light:
		# light.write(a)
		# light.flush()
		# os.fsync(light.fileno())
	sleep(1)

def room1fanON():
	GPIO.output(16,False)
	global fstatus
	fstatus="ON"
	switch['fan']='ON'
	switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(switch,f)
		f.write("\n")
	# with open("/home/pi/Python_Scripts/homeauto/r1.fan.txt","w") as fan:
		# fan.write(b)
		# fan.flush()
		# os.fsync(fan.fileno())
	sleep(1)

def room1fanOFF():
	GPIO.output(16,True)
	global fstatus
	fstatus="OFF"
	switch['fan']='OFF'
	switch['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(switch,f)
		f.write("\n")
	# with open("/home/pi/Python_Scripts/homeauto/r1.fan.txt","w") as fan:
		# fan.write(a)
		# fan.flush()
		# os.fsync(fan.fileno())
	sleep(1)

def tempshow():
	with open("/home/pi/Python_Scripts/homeauto/temperature.txt") as tem:
		temp=list(tem)[-1]
	return(temp.replace("\n",""))
def humishow():
	with open("/home/pi/Python_Scripts/homeauto/humidity.txt") as hum:
		humi=list(hum)[-1]
	return(humi.replace("\n",""))
def timeshow():
	with open("/home/pi/Python_Scripts/homeauto/timestamp.txt") as tim:
		time=list(tim)[-1]
	return time
def doorunlock():
	try:
		aio.send('door', 1)
	except:
		print("Error try again")
	

@app.route("/", methods=['GET', 'POST'])
def index():
	global lstatus
	global fstatus
	lstatus=""
	fstatus=""
	with open("/home/pi/Python_Scripts/homeauto/switch.txt") as f:
		temp=list(f)[-1]
		temp=temp.replace("\n","")
		data=json.loads(temp)
		if data["light"]=="OFF":
			lstatus="OFF"
		if data["light"]=="ON":
			lstatus="ON"
		if data["fan"]=="OFF":
			fstatus="OFF"
		if data["fan"]=="ON":
			fstatus="ON"
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

@app.route("/lightoff", methods=['POST'])
def r1lightoff():
	room1lightOFF()
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

@app.route("/lighton", methods=['POST'])
def r1lighton():
	room1lightON()
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

@app.route("/fanoff", methods=['POST'])
def fanoff():
	room1fanOFF()
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

@app.route("/fanon", methods=['POST'])
def fanon():
	room1fanON()
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

@app.route("/doorlock", methods=['POST'])
def doorlock():
	doorunlock()
	return render_template('index.html', message=getCPUtemperature(), lstat=lstatus, fstat=fstatus, temp=tempshow(), humi=humishow(), time=timeshow())

if __name__ == "__main__":
	global lstatus, fstatus
	sleep(2)
	#r1l=open("/home/pi/Projects/html/homeauto/r1.light.txt","r+")
	#r1f=open("/home/pi/Projects/html/homeauto/r1.fan.txt","r+")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt") as f:
		temp=list(f)[-1]
		temp=temp.replace("\n","")
		data=json.loads(temp)
		if data["light"]=="OFF":
			room1lightOFF()
			lstatus="OFF"
		if data["light"]=="ON":
			lstatus="ON"
		if data["fan"]=="OFF":
			room1fanOFF()
			fstatus="OFF"
		if data["fan"]=="ON":
			fstatus="ON"
	#with open("/home/pi/Projects/html/homeauto/r1.light.txt") as light:
		#ldata=light.read(1)
		#if ldata=="0":
			#room1lightOFF()
			#lstatus="OFF"
		#if ldata=="1":
			#lstatus="ON"
		#switch['light']=lstatus
		#with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
                	#json.dump(switch,f)
                	#f.write("\n")
	#with open("/home/pi/Projects/html/homeauto/r1.fan.txt") as fan:
		#fdata=fan.read(1)
		#if fdata=="0":
			#room1fanOFF()
			#fstatus="OFF"
		#if fdata=="1":
			#fstatus="ON"
		#switch['fan']=fstatus
		#with open("/home/pi/Projects/html/homeauto/switch.txt", "w") as f:
                	#json.dump(switch,f)
                	#f.write("\n")
	app.run("0.0.0.0", 5001,threaded=1)
