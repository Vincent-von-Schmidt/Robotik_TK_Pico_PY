from motor import *
from sensor_licht import *
import utime

LEDW = 18
LEDR = 19
LEDG = 20

TASTER_L = machine.Pin(16 , machine.Pin.IN, machine.Pin.PULL_DOWN)
TASTER_R = machine.Pin(17 , machine.Pin.IN, machine.Pin.PULL_DOWN)


s = Sensor(LEDW)
V = 50

print("Taste R --> Kalibrieren, losfahren")
print("Taste L --> losfahre")
print("keine Taste nach 5 sek. --> losfahren")

tasteL = TASTER_L.value()
tasteR = TASTER_R.value()

t1 = utime.ticks_ms()
while (utime.ticks_ms() - t1 < 5000) & (tasteL == 0) & (tasteR == 0):
    tasteL = TASTER_L.value()
    tasteR = TASTER_R.value()
    
if tasteR == 1:
    print("Kalibrieren ... ")
    s.kalibrierStart()
    
    for i in range(500): 
        s.kalibrierRunde()
        utime.sleep_ms(10)

    print("Kalibrieren fertig!")


utime.sleep_ms(200)
 
print("Fahre los ... Taste L --> stop")

while not TASTER_L.value() == 1:
    s.messen()
    diff = s.wertR - s.wertL
    diff = diff * 5
    #print(diff)
    OnFwd(MOT_A, V + diff)
    OnFwd(MOT_B, V - diff)
Off(MOT_AB)
print("ENDE")