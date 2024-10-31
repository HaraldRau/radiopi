from RPi import GPIO
import time
import os
import drivers
import senderliste
display = drivers.Lcd(0x27)
display.lcd_display_string("Radio Pi V 0.10", 1)
# display.lcd_display_string("Version 0.10", 2)
from threading import Thread
# os.system("mocp -S")
# os.system("mocp --volume=100")
# os.system("mocp --playit /home/hara/radiopi/ready.mp3")
# Variablen
clk = 5
dt = 6
sw = 13
counter = 0
cur_counter = 0
#max_counter = 40 # nicht mehr NOTIG weil keine Skala
activplayer = 0

#befehl = "mocp --playit "

# Senderliste LOESCHEN
#sender = ("http://sc2.radiocaroline.net:10558/",
#          "http://stream.laut.fm/1-hits70s",
#          "http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa",
#          "http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa",
#          "http://laut.fm/oldies",
#	  "http://stream.laut.fm/the-beat-goes-on",
#	  "http://stream.laut.fm/northernsoul")
# eine Umdrehung 40 klicks
# Uebersetzung von 1:4 empfohlen

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(21,GPIO.OUT) # Betriebsanzeige AN/AUS Nach Start verschieben, wenn WLAN
# GPIO.setup(20,GPIO.OUT)
# GPIO.output(21,GPIO.HIGH) # Betriebsanzeige AN/AUS Nach Start verschieben, wenn WLAN
# GPIO.output(20,GPIO.HIGH)
time.sleep(1)
# GPIO.output(20,GPIO.LOW)
display.lcd_display_string("Sender suchen!", 2)


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
		display.lcd_clear()
		#print (counter)
		cur_counter = counter
		#frequenz = int((counter/max_counter*18)+88) # Prüfen auf Notwendigkeit
		#senderID = int((frequenz-88)/2) # Frequenz ersetzen durch counter??? eventuell /4 ???
		frequenz = int(counter/4)
		senderID = int(counter/8)
		#print (counter, frequenz, senderID)
		#display.lcd_display_string(str(counter), 1)#zeile ausschalten
		#display.lcd_display_string(str(senderID), 2)#in den if-zweig verschiben und den Sender anzeigen
		#sleep(5)
		print (senderID, counter, frequenz)
		if (frequenz % 2) and activplayer == 0:
			#print (activplayer)
			sender = senderliste.sender(senderID)
			terminal = f"mocp --playit {sender[1]}"
			os.system(terminal)
			display.lcd_display_string(sender[1], 2)
			activplayer = 1
			#sleep(1)
		if not(frequenz % 2):
			#os.system("mocp --stop") #ABSCHALTEN
			activplayer = 0
