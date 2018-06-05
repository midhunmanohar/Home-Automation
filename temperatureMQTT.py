import requests
from time import sleep
import datetime
import os

url = "mosquitto_pub -d -u raspberry -P 8904416718 -t TempSensor -m "


def tempshow():
    with open("/home/pi/Projects/html/homeauto/temperature.txt") as tem:
       temp=list(tem)[-1]
    return(temp.replace("\n",""))
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))
	   
while(1):
    while True:
       try:
          os.system(url+getCPUtemperature())
          break
       except:
	  print("Connection error... retrying...")
          sleep(10)
    sleep(10)
