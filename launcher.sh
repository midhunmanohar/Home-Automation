#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd
cd /home/pi/Python_Scripts/homeauto
python /home/pi/Python_Scripts/homeauto/homeauto.py &
sudo python /home/pi/Python_Scripts/homeauto/switch.py &
#sudo python /home/pi/Projects/html/Navratri/navaratri.py &
sleep 2
sudo python /home/pi/Python_Scripts/homeauto/temperature.py &
sleep 10
sudo python /home/pi/Python_Scripts/homeauto/telegramtext.py &
#sudo python /home/pi/Python_Scripts/homeauto/telegramfantimer.py &
#sudo python /home/pi/Python_Scripts/homeauto/timer.py &
#sudo python /home/pi/Projects/html/homeauto/PIR.py &
sudo python /home/pi/Python_Scripts/homeauto/CPUtempmon.py &
sudo python /home/pi/Python_Scripts/homeauto/adafruitmqtt.py &
#sudo python /home/pi/Python_Scripts/homeauto/voltage.py &
cd
