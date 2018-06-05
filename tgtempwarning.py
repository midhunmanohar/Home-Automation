import requests
import os
from time import sleep
import telepot
from telepot.loop import MessageLoop
import urllib2

bot = telepot.Bot('398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I')
url = "https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/"

def handle():
    global check
    while True:
       try:
          chat_id = get_chat_id(last_update(get_updates_json(url)))
          break
       except:
          #print("No last message found")
          while True:
             try:
                response = requests.post('https://api.telegram.org/bot398042579:AAHsbBQLmBZkj3H0ZrZsz6ymrFt-Chxy14I/sendMessage?chat_id=395386694&text=Waiting%20for%20a%20text')
                break
             except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                sleep(10)
                print("Was a nice sleep, now let me continue...")
          sleep(10)
    command = last_update(get_updates_json(url))
    command= command['message']['text']
    if command=='/start':
       check=1
       #print(" command check = 1")
    if command=='/stop':
       check=0
       #print("command check = 0")
    if command=='/temp':
       check=2
       #print("command check = 2")

def get_updates_json(request):
    while True:
       try:
          response = requests.get(request + 'getUpdates')
          break
       except:
          print("Connection refused by the server..")
          print("Let me sleep for 5 seconds")
          print("ZZzzzz...")
          sleep(10)
          print("Was a nice sleep, now let me continue...")
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    while True:
       try:
          response = requests.post(url + 'sendMessage', data=params)
          break
       except:
          print("Connection refused by the server..")
          print("Let me sleep for 5 seconds")
          print("ZZzzzz...")
          sleep(10)
          print("Was a nice sleep, now let me continue...")
    return response

#chat_id = get_chat_id(last_update(get_updates_json(url)))
#send_mess(chat_id, 'Hello World')

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


def printtemp():
    global check
    if check==2:
       #print("/temp command")
       temp= int(float(getCPUtemperature()))
       send_mess(get_chat_id(last_update(get_updates_json(url))), 'CPU Temp: '+getCPUtemperature())


def main():
    global check
    check=1
    #print(" main check = 1")
    while True:
    #    print("While loop start i=0")
        i=0
        temp= int(float(getCPUtemperature()))
        printtemp()
        #if check==2:
        #    print("/temp command")
        #    send_mess(get_chat_id(last_update(get_updates_json(url))), 'CPU Temp: '+getCPUtemperature())
        #    check=1
        if temp>50 and check==1:
    #        print("temp>50 and check==1")
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'CPU Temp HIGH, '+getCPUtemperature())
        if temp<=48 and check !=0:
            for i in range(10):
               sleep(1)
     #          print("temp<=48 loop "+str(i))
               printtemp()
        if temp>48 and check!=0:
            for i in range(10):
               sleep(1)
     #         print("temp>48 loop "+str(i))
               printtemp()

        if check==0:
            for i in range(10):
               sleep(1)
     #          print("check==0 loop "+str(i))
               if check==2 or check==1:
     #             print("check==0 loop break")
                  printtemp()
                  break
        if temp>=60:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'CPU Temp VERY HIGH, '+getCPUtemperature())
            for i in range(10):
               sleep(1)
        handle()
if __name__ == '__main__':
    main()
