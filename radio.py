from RPi import GPIO
from time import sleep
import time
import os
from threading import Thread

clk = 17
dt = 18
counter = 0
max_counter = 40
activplayer = 0
befehl = "mplayer -ao alsa "
sender = ("http://sc2.radiocaroline.net:10558/",
          "https://nora.streamabc.net/regc-noraoldie-mp3-192-4426850",
          "http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa",
          "http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa",
          "http://laut.fm/oldies",
	  "http://stream.laut.fm/the-beat-goes-on")
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Funktion Playeraufruf
def play():
	global terminal
	os.system(terminal)


# Funktion für Tread Abfrage des Senderwählers K
def senderwahl():
        global counter
        counter = 0
        clkLastState = GPIO.input(clk)
        try:
                while True:
                        clkState = GPIO.input(clk)
                        dtState = GPIO.input(dt)
                        if clkState != clkLastState:
                                if dtState != clkState:
                                        counter += 1
                                else:
                                        counter -= 1
                                #print (counter)
                                clkLastState = clkState
        finally:
                GPIO.cleanup()

# Thread zuweisen und starten
sendersuche = Thread(target=senderwahl)
sendersuche.start()

# Sender aufwählen und abspielen
while True:
        print (counter)
        frequenz = int((counter/max_counter*18)+88)
	senderID = int((frequenz-88)/2)
	print (counter, frequenz, senderID)
        
	if (frequenz % 2) and activplayer == 0:
		terminal = befehl + sender[senderID]
		activplayer = 1
		mplayer = Thread(target=play)
		mplayer.start()
                sleep(1)
        else:
                os.system("killall mplayer")
                activplayer = 0
