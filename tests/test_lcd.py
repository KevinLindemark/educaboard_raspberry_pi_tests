# https://learn.adafruit.com/character-lcds/python-circuitpython
# pip3 install adafruit-circuitpython-charlcd
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_rs = digitalio.DigitalInOut(board.D27)
lcd_en = digitalio.DigitalInOut(board.D22)
lcd_d7 = digitalio.DigitalInOut(board.D18)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd_columns = 20
lcd_rows = 4

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
lcd_rs = digitalio.DigitalInOut(board.D26)

lcd.message = "Hello\nKEA\nIT-Technologists\nWelcome back!"

lcd.cursor = True
