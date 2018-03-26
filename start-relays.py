#!/usr/bin/python
import paho.mqtt.client as mqttClient
import RPi.GPIO as GPIO
import ConfigParser
import time
import os
relay1 = 0
relay2 = 1
relay3 = 2
relay4 = 3
relay5 = 4
relay6 = 5
relay7 = 6
relay8 = 7

pinRelays = [4,17,18,22,23,24,25,27]
pinBotones = [6,12,13,19,16,26,20,21]


def on_message(client, userdata, message):
#	print "Message received: "  + message.payload
	if message.topic == "cmnd/raspberry/POWER1":
		print("Topic",message.topic)
		if message.payload == "ON":
			print ("Commando recibido ON")
			GPIO.output(pinRelays[relay1], GPIO.HIGH)
			msgs = [{'topic': "paho/test/multiple", 'payload': "multiple 1"}, ("paho/test/multiple", "multiple 2", 0, False)]
			client.publish("stat/raspberry/POWER1","ON")
            		#print os.popen("irsend SEND_ONCE lg1 key_volumedown").read()
		if message.payload == "OFF":
			print ("Commando recibido OFF")
			GPIO.output(pinRelays[relay1], GPIO.LOW)
			client.publish("stat/raspberry/POWER1","OFF")
           	 	#print os.popen("irsend SEND_ONCE lg1 key_volumeup").read()
	if message.topic == "cmnd/raspberry/POWER2":
                print("Topic",message.topic)
		if message.payload == "ON":
                	print ("Commando recibido ON" )
                	GPIO.output(pinRelays[relay2], GPIO.HIGH)
			client.publish("stat/raspberry/POWER2","ON")
                if message.payload == "OFF":
                	print ("Commando recibido OFF")
                	GPIO.output(pinRelays[relay2], GPIO.LOW)
			client.publish("stat/raspberry/POWER2","OFF")
        if message.topic == "cmnd/raspberry/POWER3":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay3], GPIO.HIGH)
			client.publish("stat/raspberry/POWER3","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay3], GPIO.LOW)
			client.publish("stat/raspberry/POWER3","OFF")
        if message.topic == "cmnd/raspberry/POWER4":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay4], GPIO.HIGH)
			client.publish("stat/raspberry/POWER4","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay4], GPIO.LOW)
			client.publish("stat/raspberry/POWER4","OFF")
        if message.topic == "cmnd/raspberry/POWER5":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay5], GPIO.HIGH)
			client.publish("stat/raspberry/POWER5","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay5], GPIO.LOW)
			client.publish("stat/raspberry/POWER5","OFF")
        if message.topic == "cmnd/raspberry/POWER6":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay6], GPIO.HIGH)
			client.publish("stat/raspberry/POWER6","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay6], GPIO.LOW)
			client.publish("stat/raspberry/POWER6","OFF")
        if message.topic == "cmnd/raspberry/POWER7":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay7], GPIO.HIGH)
			client.publish("stat/raspberry/POWER7","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay7], GPIO.LOW)
			client.publish("stat/raspberry/POWER7","OFF")
        if message.topic == "cmnd/raspberry/POWER8":
                print("Topic",message.topic)
                if message.payload == "ON":
                        print ("Commando recibido ON" )
                        GPIO.output(pinRelays[relay8], GPIO.HIGH)
			client.publish("stat/raspberry/POWER8","ON")
                if message.payload == "OFF":
                        print ("Commando recibido OFF")
                        GPIO.output(pinRelays[relay8], GPIO.LOW)
			client.publish("stat/raspberry/POWER8","OFF")
def mfp1(channel):
   if GPIO.input(pinBotones[relay1]):
	print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay1])))
        GPIO.output(pinRelays[relay1], GPIO.HIGH)
   else:
	print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay1])))
        GPIO.output(pinRelays[relay1], GPIO.LOW)
def mfp2(channel):
   if GPIO.input(pinBotones[relay2]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay2])))
        GPIO.output(pinRelays[relay2], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay1])))
        GPIO.output(pinRelays[relay1], GPIO.LOW)
def mfp3(channel):
   if GPIO.input(pinBotones[relay3]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay3])))
        GPIO.output(pinRelays[relay3], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay3])))
        GPIO.output(pinRelays[relay3], GPIO.LOW)
def mfp4(channel):
   if GPIO.input(pinBotones[relay4]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay4])))
        GPIO.output(pinRelays[relay4], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay4])))
        GPIO.output(pinRelays[relay4], GPIO.LOW)
def mfp5(channel):
   if GPIO.input(pinBotones[relay5]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay5])))
        GPIO.output(pinRelays[relay5], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay5])))
        GPIO.output(pinRelays[relay5], GPIO.LOW)
def mfp6(channel):
   if GPIO.input(pinBotones[relay6]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay6])))
        GPIO.output(pinRelays[relay6], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay6])))
        GPIO.output(pinRelays[relay6], GPIO.LOW)
def mfp7(channel):
   if GPIO.input(pinBotones[relay7]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay7])))
        GPIO.output(pinRelays[relay7], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay7])))
        GPIO.output(pinRelays[relay7], GPIO.LOW)
def mfp8(channel):
   if GPIO.input(pinBotones[relay8]):
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay8])))
        GPIO.output(pinRelays[relay8], GPIO.HIGH)
   else:
        print("mfp: channel={} is {}".format(channel, GPIO.input(pinBotones[relay8])))
        GPIO.output(pinRelays[relay8], GPIO.LOW)

########################mqtt inicio####################################
def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

#print("message received " ,str(message.payload.decode("utf-8")))
#    print("message topic=",message.topic)
# print("message qos=",message.qos)
# print("message retain flag=",message.retain)

config = ConfigParser.ConfigParser()
config.read("config.ini")
try:

	brokerIp = config.get("brokerVars", "broker")
	brokerUser = config.get("brokerVars", "username")
	brokerPasswd = config.get("brokerVars", "password")
	brokerPort = config.get("brokerVars", "port")
except ConfigParser.NoOptionError :
	print ("Error al leer la configuracion de mqtt")
	
Connected = False   #global variable for the state of the connection
broker_address= brokerIp  #Broker address
port = brokerPort                         #Broker port
user = brokerUser                    #Connection username
password = brokerPasswd            #Connection password

client=mqttClient.Client("",True,None,mqttClient.MQTTv31)              #create n             ew instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("+/raspberry/#")
#########################mqtt fin ######################################
GPIO.setmode(GPIO.BCM)
for i in pinRelays:
   GPIO.setup(i, GPIO.OUT)
   GPIO.output(i, GPIO.LOW)
for Y in pinBotones:
   GPIO.setup(Y,GPIO.IN)
try:
	GPIO.add_event_detect(pinBotones[relay1], GPIO.BOTH, callback=mfp1)
	GPIO.add_event_detect(pinBotones[relay2], GPIO.BOTH, callback=mfp2)
	GPIO.add_event_detect(pinBotones[relay3], GPIO.BOTH, callback=mfp3)
	GPIO.add_event_detect(pinBotones[relay4], GPIO.BOTH, callback=mfp4)
	GPIO.add_event_detect(pinBotones[relay5], GPIO.BOTH, callback=mfp5)
	GPIO.add_event_detect(pinBotones[relay6], GPIO.BOTH, callback=mfp6)
	GPIO.add_event_detect(pinBotones[relay7], GPIO.BOTH, callback=mfp7)
	GPIO.add_event_detect(pinBotones[relay8], GPIO.BOTH, callback=mfp8)
#	GPIO.add_event_detect(pinBotones[relay], GPIO.FALLING, callback=suelto)
#	GPIO.add_event_detect(Input_Sig, GPIO.FALLING, callback=interrupt_service_routine, bouncetime=5)
	while True:
		time.sleep(60)
except KeyboardInterrupt:
  print "chaitoo......."
  client.disconnect()
  client.loop_stop()
  GPIO.cleanup() # limpiando los gpio

