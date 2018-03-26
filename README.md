# Poyecto raspberrypi-8relays
Raspberry pi zero w + 8 relay + 8 botones controlado con mqtt

#He creado este proyecto en python 2.7 para controlar 8 relays y 8 pulsadores con un Raspberry pi zero w mediante el protocolo mqtt. todo #esto para controllar las luces de un segundo piso de mi casa :)

#Ademas de integrar el proyecto con openhab2 y echo de amazon.

#Pin de los relays BCM 4,17,18,22,23,24,25,27 ver imagen PiZero_1.png
#Pin de Botones BCM 6,12,13,19,16,26,20,21 configuracion pulldown con resistencas de 10k y de 1k al gpio.
#PUlldown =  3.3v pin  ----- 10k------- negativo + 1k ----- GPIO

# mqtt topic 
#+/raspberry/#
# comandos
#cmnd/raspberry/POWER1 ON or OFF
#cmnd/raspberry/POWER2 ON or OFF
#cmnd/raspberry/POWER3 ON or OFF
#cmnd/raspberry/POWER4 ON or OFF
#cmnd/raspberry/POWER5 ON or OFF
#cmnd/raspberry/POWER6 ON or OFF
#cmnd/raspberry/POWER7 ON or OFF
#cmnd/raspberry/POWER8 ON or OFF 

# comando para test desde servidor mqtt:
#mosquitto_pub -h localhost -t cmnd/raspberry/POWER1 -m 'OFF' -u username -P password  -p 17388

#  librerias 
#pip install paho-mqtt 
#
# Ejemplos de como utilizar mqtt
#https://pypi.python.org/pypi/paho-mqtt/1.1  
#http://www.steves-internet-guide.com/into-mqtt-python-client/

# Ejemplo de como detectar una interrupcion 
#https://raspberrypi.stackexchange.com/questions/62035/using-gpio-from-cli-to-trigger-a-rising-or-falling-event-detection
# 
# loop para los iniciar los relays
#https://www.raspberrypi.org/forums/viewtopic.php?t=167018
#https://stackoverflow.com/questions/19749497/how-can-i-set-pin-3-to-high-then-pin-2-with-a-raspberry-pi
