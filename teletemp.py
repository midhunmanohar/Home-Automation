import sys
import time
import random
import datetime
import telepot
import os
from telepot.loop import MessageLoop

bot = telepot.Bot('398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I')

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    t= str(datetime.datetime.now().strftime("%-S"))
    if command=='/temp':
       bot.sendMessage(chat_id, text="CPU Temp: "+getCPUtemperature())
    while False:
       time.sleep(1)
       t= int(datetime.datetime.now().strftime("%-S"))
       if t in (0, 10, 20, 30, 40, 50):
          t=str(t)
          bot.sendMessage(chat_id, text="This is a test msg"+t)

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)