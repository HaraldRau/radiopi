from RPi import GPIO
from time import sleep
import time
from threading import Thread

clk = 17
dt = 18
befehl = "mplayer -ao alsa "
sender = ("http://sc2.radiocaroline.net:10558/","https://nora.streamabc.net/regc-noraoldie-mp3-192-4426850","http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa","http://laut.fm/oldies","https://stream.laut.fm/the-beat-goes-on")
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
        if counter < 0:
                counter = 0
        if counter > 80:
                counter =80
        print (counter)
        if counter < 10 and counter > 5:
                print (sender[0])
                play = befehl  + sender[0]
                os.system(play)
        elif counter < 20 and counter > 15:
                print (sender[1])
                play = befehl  + sender[1]
                os.system(play)
        elif counter < 30 and counter > 25:
                print (sender[2])
                play = befehl  + sender[2]
                os.system(play)
        elif counter < 40 and counter > 35:
                print (sender[3])
                play = befehl  + sender[3]
                os.system(play)
        elif counter < 50 and counter > 45:
                print (sender[4])
                play = befehl  + sender[4]
                os.system(play)
        elif counter < 60 and counter > 55:
                print (sender[5])
                play = befehl  + sender[5]
                os.system(play)
        else:
                print ("kein Sender aktiv")
                try:
                        os.system('killall mplayer')
        sleep(1)

