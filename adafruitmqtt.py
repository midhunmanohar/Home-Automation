# Example of using the MQTT client class to subscribe to and publish feed values.
# Author: Tony DiCola

# Import standard python modules.
import random
import sys
import time
import RPi.GPIO as GPIO
import os
import datetime
import sys
import json

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = '1843a8e537fe47a98d6e0907e8001d6f'
ADAFRUIT_IO_USERNAME = 'midhunmanohar'  # See https://accounts.adafruit.com
                                                    # to find your username.
def switchstatus():
    with open("/home/pi/Python_Scripts/homeauto/switch.txt") as f:
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
    with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
	json.dump(data,f)
	f.write("\n")

def switchon():
   GPIO.output(11, 0)
   GPIO.output(16, 0)
   switchstatus()
   global data
   data['light']='ON'
   data['fan']='ON'
   data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
   with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
	json.dump(data,f)
	f.write("\n")

def room1lightON():
	GPIO.output(11, 0)
	switchstatus()
	global data
	data['light']='ON'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
		
def room1lightOFF():
	GPIO.output(11, 1)
	switchstatus()
	global data
	data['light']='OFF'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
		
def room1fanON():
	GPIO.output(16, 0)
	switchstatus()
	global data
	data['fan']='ON'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
		
def room1fanOFF():
	GPIO.output(16, 1)
	switchstatus()
	global data
	data['fan']='OFF'
	data['time']= datetime.datetime.now().strftime("%d %b %Y %H:%M")
	with open("/home/pi/Python_Scripts/homeauto/switch.txt", "w") as f:
		json.dump(data,f)
		f.write("\n")
		
		
# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    #print('Connected to Adafruit IO!  Listening for DemoFeed changes...')
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('home')

def disconnected(client):
    #Disconnected function will be called when the client disconnects.
    print('Disabled: Disconnect from Adafruit IO!')
    #sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if payload=='0':
	room1lightON()
    if payload=='1':
	room1lightOFF()
    if payload=='2':
	room1fanON()
    if payload=='3':
	room1fanOFF()
    if payload=='4':
        switchon()
    if payload=='5':
	switchoff()


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
#client.loop_background()
# Now send new values every 10 seconds.
#print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
#while True:
#    value = random.randint(0, 100)
#    print('Publishing {0} to DemoFeed.'.format(value))
#    client.publish('g6-home', value)
#    time.sleep(10)

# Another option is to pump the message loop yourself by periodically calling
# the client loop function.  Notice how the loop below changes to call loop
# continuously while still sending a new message every 10 seconds.  This is a
# good option if you don't want to or can't have a thread pumping the message
# loop in the background.
#last = 0
#print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
#while True:
#   # Explicitly pump the message loop.
#   client.loop()
#   # Send a new message every 10 seconds.
#   if (time.time() - last) >= 10.0:
#       value = random.randint(0, 100)
#       print('Publishing {0} to DemoFeed.'.format(value))
#       client.publish('DemoFeed', value)
#       last = time.time()

# The last option is to just call loop_blocking.  This will run a message loop
# forever, so your program will not get past the loop_blocking call.  This is
# good for simple programs which only listen to events.  For more complex programs
# you probably need to have a background thread loop or explicit message loop like
# the two previous examples above.
client.loop_blocking()
