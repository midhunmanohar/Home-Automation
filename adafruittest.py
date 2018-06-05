from Adafruit_IO import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

aio = Client('1843a8e537fe47a98d6e0907e8001d6f')
mqtt = MQTTClient('1843a8e537fe47a98d6e0907e8001d6f')

data = aio.receive('Light')
if data=='0'
	GPIO.output(11, 0)
if data=='1'
	GPIO.output(11, 1)
