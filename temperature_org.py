import sys
import os
import Adafruit_DHT
from time import sleep
import datetime


while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 26)

    #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    temp = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    time =  datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    with open("/home/pi/Projects/html/homeauto/temperature.txt","a") as tem:
       tem.write(temp + ", Last updated at " + time +"\n")
       tem.flush()
       os.fsync(tem.fileno())
    sleep(600)
    
 