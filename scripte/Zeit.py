import tm1637
import datetime
import time

display = tm1637.TM1637(clk=27, dio=17)

# 1. Aktuelles Datum und Uhrzeit abrufen
while True:
	jetzt = datetime.datetime.now()
	display.numbers(jetzt.hour,jetzt.minute)
	time.sleep(30)
