# eksempel er her fra: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
# Bemærk - eksemplet virker ikke på Educaboard da Neopixels skal side på gpio 10 som har SPI
# documentation: https://docs.circuitpython.org/projects/neopixel/en/latest/
import board
import neopixel

DATA_PIN = board.D10
pixel = neopixel.NeoPixel(DATA_PIN, 12)

for i in range(12):
    print(i)
    pixel[i] = (30, i*3, 20)
