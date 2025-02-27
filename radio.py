from RPi import GPIO
import time
import os
import drivers
import senderliste
import atexit
display = drivers.Lcd(0x27)
display.lcd_display_string("Radio Pi V 0.90", 1)
from threading import Thread

# Variablen ====================================================================
clk = 5
dt = 6
sw = 13
counter = 0
cur_counter = 0
activplayer = 0
mode = 0 # mode 0 -> Internetsender mode 1 -> USB-Stick über Playliste mode 3 -> dnla-Server

# GPIO einrichten =============================================================

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
display.lcd_display_string("Radio ON!", 2)
time.sleep(2)
os.system('mocp -p')

# Automatische Bereinigung bei Beenden des Programms ==========================
atexit.register(GPIO.cleanup)

# Funktion für Tread Abfrage des Senderwählers K ==============================
def senderwahl():
	global counter
	global mode
	global activeplayer
	counter = 0
	mode = 0
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

				#==Radio==
				display.lcd_clear()
				display.lcd_display_string("RADIO          ", 1)
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("RADIO ON      ", 2)
					time.sleep(1)
					activeplayer = 0
					mode = 0
					os.system('mocp -P')
					counter = 1
					cur_counter = 0
					display.lcd_clear()

				#==USB Play==
				display.lcd_clear()
				display.lcd_display_string("USB Play      ", 1)
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("mocp -p       ", 2)
					time.sleep(1)
					mode = 2
					os.system('mocp -p')
					display.lcd_clear()
				
				#==USB Playliste==
				display.lcd_clear()
				display.lcd_display_string("USB Playliste  ", 1)
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("sudo mount USB ", 2)
					time.sleep(1)
					mode = 1
					display.lcd_clear()
				
				#==Neustart==
				display.lcd_clear()
				display.lcd_display_string("Neustart       ", 1)
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("sudo reboot     ", 2)
					time.sleep(1)
					os.system('sudo reboot')

				#==Anhalten==
				display.lcd_clear()
				display.lcd_display_string("Anhalten       ", 1)
				time.sleep(1)
				if GPIO.input(sw) == 0:
					display.lcd_display_string("sudo halt -p    ", 2)
					time.sleep(1)
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
	while mode == 0:
		#print(counter,cur_counter)
		#print(mode)
		if counter < 0:
			counter = 0
		while cur_counter != counter:
			cur_counter = counter
			frequenz = int(counter/2)
			senderID = int(counter/4)
			if (frequenz % 2) and activplayer == 0:
				#print (activplayer)
				sender = senderliste.sender(senderID)
				terminal = f"mocp --playit {sender[1]}"
				os.system(terminal)
				os.system('mocp -v 85')
				anzeige = sender[0]
				display.lcd_clear()
				display.lcd_display_string(anzeige, 2)
				display.lcd_display_string("Radio ON", 1)
				activplayer = 1
			if not(frequenz % 2):
				activplayer = 0
	while mode == 1:
		try:
			os.system('sudo mount /dev/sda /home/hara/usb')
		finally:
			time.sleep(4)
			display.lcd_display_string("USB Play", 1)
		os.system('mocp -P')
		os.system('mocp -a /home/hara/usb/')
		os.system('mocp -p')
		os.system('mocp -v 100')
		time.sleep(2)
		mode = 2
	while mode == 2:
		time.sleep(10)
