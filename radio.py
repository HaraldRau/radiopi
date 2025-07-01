from RPi import GPIO
import time
import os
import drivers
import senderliste
import atexit
import subprocess
display = drivers.Lcd(0x27)
display.lcd_display_string("Radio Pi V 1.01", 1)
from threading import Thread

# Variablen ====================================================================
clk = 5
dt = 6
sw = 13
counter = 0
cur_counter = 0
activplayer = 0

# GPIO einrichten =============================================================
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
display.lcd_display_string("Playlist ON!", 2)
time.sleep(2)
os.system('mocp -p')
os.system('mocp -v 100')

# Automatische Bereinigung bei Beenden des Programms ==========================
atexit.register(GPIO.cleanup)

# Funktion für Tread Abfrage des Senderwählers K ==============================
def senderwahl():
	global counter
	counter = 0
	clkLastState = GPIO.input(clk)
	try:
		while True:
			time.sleep(0.005)
			clkState = GPIO.input(clk)
			dtState = GPIO.input(dt)
			if clkState != clkLastState:
				if dtState != clkState:
					counter += 1
				else:
					counter -= 1
			clkLastState = clkState
			if GPIO.input(sw) == 0:
				#==PAUSE==
				os.system('mocp -G')
				
				#==Anhalten==
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_clear()					
					display.lcd_display_string("Herunterfahren  ", 1)
					time.sleep(1)
					display.lcd_backlight(0)
					os.system('sudo halt -p')
				
				
	finally:
		GPIO.cleanup()

# Thread zuweisen und starten ==================================================
sendersuche = Thread(target=senderwahl)
sendersuche.start()

# Hauptprogramm ================================================================
while True:
	time.sleep(0.005)
	if counter < 0:
		counter = 0
	while cur_counter != counter:
		cur_counter = counter
		frequenz = int(counter/2)
		senderID = int(counter/4)
		if (frequenz % 2) and activplayer == 0:
			sender = senderliste.sender(senderID)
			terminal = f"mocp --playit {sender[1]}"
			os.system(terminal)
			anzeige = sender[0]
			display.lcd_clear()
			display.lcd_display_string(anzeige, 1)
			display.lcd_display_string("Radio ON!       ", 2)
			activplayer = 1
		if not(frequenz % 2):
			activplayer = 0
