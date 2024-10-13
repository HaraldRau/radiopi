import drivers
import time
display = drivers.Lcd(0x27)
try:
  while True:
    print("look at display")
    display.lcd_display_string("Demo line 1", 1)
    display.lcd_display_string("Demo line 2", 2)
    display.lcd_display_string("Demo line 3", 3)
    display.lcd_display_string("Demo line 4", 4)
    time.sleep(2) # Give time for the message to be read
    display.lcd_clear() # Clear the display of any data
    time.sleep(2) # Give time for the message to be read
except KeyboardInterrupt:
  # exit on KeyboardInterrupt (when you press ctrl+c)
  print("exit")
  display.lcd_clear()
