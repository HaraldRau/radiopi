from RPi import GPIO
from time import sleep
import time
from threading import Thread

clk = 17
dt = 18
befehl = "mplayer -ao alsa "
sender = ("http://sc2.radiocaroline.net:10558/","https://nora.streamabc.net/regc-noraoldie-mp3-192-4426850","http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa","http://laut.fm/oldies")
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
sendersuche = Thread(target=senderwahl)
sendersuche.start()
while True:
        print (counter)        
        if counter < 10 and counter > 5:
                print (sender[0])
                play = befehl  + sender[0]
                os.system(play)
        elif counter < 20 and counter > 15:
                print (sender[1])
        elif counter < 30 and counter > 25:
                print (sender[2])
        else:
                print ("kein Sender aktiv")
                try:
                        os.system('killall mplayer')
        sleep(1)

