import drivers
import time
display = drivers.Lcd(0x27)
try:
  while True:
    print("look at display")
    display.lcd_display_string("Demo line 1", 1)
    display.lcd_display_string("Demo line 2", 2)
    display.lcd_clear() # Clear the display of any data
    time.sleep(2)
    zeit = time.ctime()
    display.lcd_display_string(zeit[11:16], 1)
    display.lcd_display_string(zeit[20:24], 2)
    time.sleep(2) # Give time for the message to be read
    display.lcd_clear() # Clear the display of any data
    time.sleep(2) # Give time for the message to be read
except KeyboardInterrupt:
  # exit on KeyboardInterrupt (when you press ctrl+c)
  print("exit")
  display.lcd_clear()
