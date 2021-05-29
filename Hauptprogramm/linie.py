from motor import *
from sensor_licht import *
import utime

s = Sensor(18)
V = 50

#s.setMinMax(20, 6000, 20, 6000)
s.kalibrierStart()

#print(utime.ticks_ms())
for i in range(500): 
    s.kalibrierRunde()
    utime.sleep_ms(10)
#print(utime.ticks_ms())
#print(s.miniL, s.maxiL, s.miniR, s.maxiR)

#print("")

#print(utime.ticks_ms())
for i in range(10000): 
    s.messen()
#print(utime.ticks_ms())

while True:
    s.messen()
    diff = s.wertR - s.wertL
    diff = diff * 5
    #print(diff)
    OnFwd(MOT_A, V + diff)
    OnFwd(MOT_B, V - diff)
