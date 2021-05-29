from motor import *
from sensor_licht import *
import utime

LEDW = 18
LEDR = 19
LEDG = 20

TASTER_L = machine.Pin(16 , machine.Pin.IN)
TASTER_R = machine.Pin(17 , machine.Pin.IN)

s = Sensor(LEDW)
V = 50

if TASTER_R.value(1): 
    print("Kalibrieren ... ")
    #s.setMinMax(20, 6000, 20, 6000)
    s.kalibrierStart()

    #print(utime.ticks_ms())
    for i in range(500): 
        s.kalibrierRunde()
        utime.sleep_ms(10)
    #print(utime.ticks_ms())
    #print(s.miniL, s.maxiL, s.miniR, s.maxiR)

    print("Kalibrieren fertig!")

if TASTER_L.value(1):
    print("Start ...")

#print(utime.ticks_ms())
for i in range(10000): 
    s.messen()
#print(utime.ticks_ms())

while True:
    s.messen()
    if TASTER_L.value(1) or TASTER_R.value(1):
        #Dose umfahren
        print("Test")
    else: 
        diff = s.wertR - s.wertL
        diff = diff * 5
        #print(diff)
        OnFwd(MOT_A, V + diff)
        OnFwd(MOT_B, V - diff)
    


