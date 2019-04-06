import serial
from time import sleep
import requests

#ser=serial.Serial('/dev/ttyS0',115200)
url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text="

#R1=30000
#R2=7500
voltage = 0.0
sum = 0
sample_count = 0
num_samples = 10
ser=serial.Serial('/dev/ttyS0',115200)
#text = GPIO.input(10)
#print (text)
while (sample_count < num_samples):
   sum = sum + int(ser.readline().replace("\n",""))
   sample_count = sample_count + 1
try:
   #voltage = int(ser.readline().replace("\n",""))
   #voltage = (float(sum)/float(num_samples)*3.93)/1023
   #voltage = (float(sum)/float(num_samples)*3.3)/1023
   voltage = (float(sum)/float(num_samples)*4.75)/1023
   #print sum
   print(voltage)
   #voltage = (3.8*voltage*(R1+R2))/(1023*R2)
   voltage = voltage*4.95
   #voltage = voltage*5.2
   print(voltage)
except:
   print("Sensor down")
try:
   if voltage>12.9:
	  #print("")
	  #requests.get(url+'Battery Voltage update: '+'{0:0.1f}'.format(voltage))
		  requests.get(url+'Battery Charge: 100% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.7 and voltage <12.9:
	  requests.get(url+'Battery Charge: 100% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.5 and voltage <12.7:
	  requests.get(url+'Battery Charge: 90% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.4 and voltage <12.5:
	  requests.get(url+'Battery Charge: 80% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.3 and voltage <12.4:
	  requests.get(url+'Battery Charge: 70% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.2 and voltage <12.3:
	  requests.get(url+'Battery Charge: 60% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>12.0 and voltage <12.2:
	  requests.get(url+'Battery Charge: 50% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>11.9 and voltage <12.0:
	  requests.get(url+'Battery Charge: 40% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage>11.7 and voltage <11.9:
	  requests.get(url+'Battery Charge: 30% \n'+'{0:0.1f}'.format(voltage)+'V')
   if voltage <11.7:
	  requests.get(url+'Battery Charge Critical: 20% \n'+'{0:0.1f}'.format(voltage)+'V')
   print ('{0:0.1f}'.format(voltage))
except:
   print("Connection error... retrying...")
#print (ser.readline())

sum = 0
sample_count = 0
#sleep(30)
