from gpiozero import PWMLED
from time import sleep

led = PWMLED(13)

while True:
    for b in range(101):
        led.value = b / 100.0
        sleep(0.01)
                        
    for b in range(100, 1, -1):
        led.value = b / 100.0
        sleep(0.01)
