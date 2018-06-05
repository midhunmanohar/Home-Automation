#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd
cd /home/pi/Projects/html/homeauto
sudo python3 /home/pi/Projects/html/homeauto/homeauto.py &
sudo python3 /home/pi/Projects/html/homeauto/switch.py &
#sudo python /home/pi/Projects/html/Navratri/navaratri.py &
sleep 2
sudo python /home/pi/Projects/html/homeauto/temperature.py &
sleep 10
sudo python /home/pi/Projects/html/homeauto/telegramtext.py &
sudo python /home/pi/Projects/html/homeauto/telegramfantimer.py &
sudo python /home/pi/Projects/html/homeauto/timer.py &
#sudo python /home/pi/Projects/html/homeauto/PIR.py &
sudo python /home/pi/Projects/html/homeauto/CPUtempmon.py &
sudo python /home/pi/Projects/html/homeauto/adafruitmqtt.py &
sudo python /home/pi/Projects/html/homeauto/voltage.py &
cd
