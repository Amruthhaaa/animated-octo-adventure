import time
from machine import Pin
import neopixel

neo=neopixel.NeoPixel(Pin(5),16) #assignpin 4 to neopixel which has 16 leds

neo[5]=(255,0,0) #RGB value
neo[10]=(0,0,255)
neo[15]=(0,255,0)
neo.write()

#neopixel connection:
#5v to 3v3 in ESP32
#GND TO GND IN ESP32#DI TO ANY GPIO'S (PIN 4 IN THIS CASE)

