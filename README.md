# Poyecto raspberrypi-8relays
Raspberry pi zero w + 8 relay + 8 botones controlado con mqtt

#He creado este proyecto en python 2.7 para controlar 8 relays y 8 pulsadores con un Raspberry pi zero w mediante el protocolo mqtt. todo #esto para controllar las luces de un segundo piso de mi casa :)

#Ademas de integrar el proyecto con openhab2 y echo de amazon.

# 

#  librerias 
#  pip install paho-mqtt 
#
# Ejemplos de como utilizar mqtt
# https://pypi.python.org/pypi/paho-mqtt/1.1  
# http://www.steves-internet-guide.com/into-mqtt-python-client/
#
#
# Ejemplo de como detectar una interrupcion 
# https://raspberrypi.stackexchange.com/questions/62035/using-gpio-from-cli-to-trigger-a-rising-or-falling-event-detection
# 
# loop para los iniciar los relays
#https://www.raspberrypi.org/forums/viewtopic.php?t=167018
# https://stackoverflow.com/questions/19749497/how-can-i-set-pin-3-to-high-then-pin-2-with-a-raspberry-pi
