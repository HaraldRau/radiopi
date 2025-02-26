import os
import time
os.system('sudo /etc/init.d/radiopi stop')
time.sleep(1)
os.system('sudo /etc/init.d/radiopi start')
