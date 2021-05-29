from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

from meinePins import *
from NeigungsSensor import *
ns=NeigungsSensor()
i2c = I2C(0, scl=Pin(5), sda=Pin(4),  freq=200000)       
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) 
print("I2C Configuration: "+str(i2c))                   
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.text("Bestimme Offset",5,8)
oled.show()
utime.sleep(1)
ns.messeOffset()
oled.fill(0)

while True:
    oled.fill(0)
    ns.messeNeigung()
    ry=ns.acc_x+32
    rx=ns.acc_y+64
    print(ns.acc_x,ns.acc_y)
    oled.line(0,32,128,32,0xffff)
    oled.line(64,0,64,68,0xffff)
    oled.rect(rx-4,ry-4,8,8,0xffff)
    oled.show()
    
    
    
    