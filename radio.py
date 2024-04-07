from RPi import GPIO
from time import sleep
import time
import os
from threading import Thread
os.system("mocp -S")
os.system("mocp --volume=100")
os.system("mocp --playit /home/hara/radiopi/ready.mp3")
# Variablen
clk = 17
dt = 18
counter = 0
cur_counter = 0
max_counter = 40
activplayer = 0

befehl = "mocp --playit "

# Senderliste
sender = ("http://sc2.radiocaroline.net:10558/",
          "http://stream.laut.fm/1-hits70s",
          "http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa",
          "http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa",
          "http://laut.fm/oldies",
	  "http://stream.laut.fm/the-beat-goes-on",
	  "http://stream.laut.fm/northernsoul")
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

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

# Dauerschleife
while True:
	# print(counter, cur_counter)
	# Sender aufwählen und abspielen
	if counter < 0:
		counter = 0
	while cur_counter != counter:
		mpplayer = Thread(target=play)
		#print (counter)
		cur_counter = counter
		frequenz = int((counter/max_counter*18)+88)
		senderID = int((frequenz-88)/2)
		#print (counter, frequenz, senderID)
		#sleep(5)
		#print (activplayer, counter, frequenz)
		if (frequenz % 2) and activplayer == 0:
			#print (activplayer)
			terminal = befehl + sender[senderID]
			mpplayer.start()
			activplayer = 1
			#sleep(1)
		if not(frequenz % 2):
			os.system("mocp --stop")
			activplayer = 0
