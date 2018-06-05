import urllib
from time import sleep
while True:
    try:
       urllib.request.urlopen('https://push2mebot.herokuapp.com/395386694/ThisisamessagefromPython')
       print("Message Sent")
       break
    except:
       print("Retrying")
       time.sleep(10)
