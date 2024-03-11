from RPi import GPIO
from time import sleep
import time
from threading import Thread

clk = 17
dt = 18
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#counter = 0
#clkLastState = GPIO.input(clk)

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
        sleep(10)
        #os.system('mplayer -ao alsa http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa')
        #os.system('killall mplayer')
        #befehl = "mplayer -ao alsa"
        #befehl = befehl + 'http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa'

