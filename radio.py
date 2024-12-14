from RPi import GPIO
import time
import os
import drivers
import senderliste
import atexit
display = drivers.Lcd(0x27)
display.lcd_display_string("Radio Pi V 0.10", 1)
from threading import Thread

# Variablen ====================================================================
clk = 5
dt = 6
sw = 13
counter = 0
cur_counter = 0
activplayer = 0
menue = 1

# GPIO einrichten =============================================================

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
display.lcd_display_string("Sender suchen!", 2)

# Automatische Bereinigung bei Beenden des Programms ==========================
atexit.register(GPIO.cleanup)

# Funktion für Tread Abfrage des Senderwählers K ==============================
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
			if GPIO.input(sw) == 0:
				print(GPIO.input(sw))
				display.lcd_display_string("-----Restart----", 2)
				time.sleep(2)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("Neustart Radio", 1)
					time.sleep(2)
					os.system('sudo reboot')
				display.lcd_display_string("-----Halt-------", 2)
				time.sleep(2)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("Anhalten Radio", 1)
					time.sleep(2)
					display.lcd_backlight(0)
					os.system('sudo halt -p')
				display.lcd_clear()
				
	finally:
		GPIO.cleanup()

# Thread zuweisen und starten ==================================================
sendersuche = Thread(target=senderwahl)
sendersuche.start()

# Hauptprogramm ===============================================================
while True:
	# print(counter, cur_counter)
	if counter < 0:
		counter = 0
	while cur_counter != counter:
		#print (counter)
		cur_counter = counter
		frequenz = int(counter/2)
		senderID = int(counter/4)
		#print (counter, frequenz, senderID)
		#display.lcd_display_string(str(counter), 1)# debug
		#display.lcd_display_string(str(senderID), 2)# debug
		#print (senderID, counter, frequenz) # debug
		if (frequenz % 2) and activplayer == 0:
			#print (activplayer)
			sender = senderliste.sender(senderID)
			terminal = f"mocp --playit {sender[1]}"
			os.system(terminal)
			os.system('mocp -v 80')
			anzeige = sender[0]
			display.lcd_clear()
			display.lcd_display_string(anzeige, 2)
			activplayer = 1
		if not(frequenz % 2):
			activplayer = 0
