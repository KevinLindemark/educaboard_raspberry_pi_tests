import time
#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

print("GPS PPS interrupt\n")
# test pin 16 for interrupt til GPSPPS
# test pin 5 for interrupt til port expander 
BUTTON_GPIO = 16

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
start = time.time()
def interrupt_GPS_PPS(channel):
    ticks = time.time() - start
    print("PPS! %d" % ticks)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, 
            callback=interrupt_GPS_PPS, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()



