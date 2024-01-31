#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

# test pin 16 for interrupt til GPSPPS
# test pin 5 for interrupt til port expander 
BUTTON_GPIO = 5

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback(channel):
    print("Button pressed!")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()