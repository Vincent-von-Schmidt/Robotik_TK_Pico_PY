from motor import *
from sensor_licht import *
import utime
from fahren import *

LEDW = 18
LEDR = 19
LEDG = 20


def MinMaxSpeichern(min1, max1, min2, max2):
    f = open('kal.txt', 'w')
    f.write(str(min1)+"\n")
    f.write(str(max1)+"\n")
    f.write(str(min2)+"\n")
    f.write(str(max2)+"\n")
    f.close()

def leseMinMax(sensor):
    try: 
        f = open('kal.txt', 'r')
        min1 = int(f.readline())
        max1 = int(f.readline())
        min2 = int(f.readline())
        max2 = int(f.readline())
        sensor.setMinMax(min1, max1, min2, max2)
        sensor.printMinMax()
        f.close()
    except:
        print("no kal data found...")
    


TASTER_L = machine.Pin(16 , machine.Pin.IN, machine.Pin.PULL_DOWN)
TASTER_R = machine.Pin(17 , machine.Pin.IN, machine.Pin.PULL_DOWN)






Off(MOT_AB)

s = Sensor(LEDW)
V = 50

leseMinMax(s)

led = machine.Pin(LEDG , machine.Pin.OUT)
led.value(1)
utime.sleep_ms(300)
led.value(0)

print("Taste R --> Kalibrieren, losfahren")
print("Taste L --> losfahre")
print("keine Taste nach 5 sek. --> losfahren")

tasteL = TASTER_L.value()
tasteR = TASTER_R.value()

t1 = utime.ticks_ms()
while (tasteL == 0) & (tasteR == 0):
    tasteL = TASTER_L.value()
    tasteR = TASTER_R.value()
    
if tasteR == 1:
    print("Kalibrieren ... ")
    s.kalibrierStart()
    
    for i in range(500): 
        s.kalibrierRunde()
        utime.sleep_ms(10)

    print("Kalibrieren fertig!")
    s.printMinMax()
    MinMaxSpeichern(s.miniL, s.maxiL, s.miniR, s.maxiR)
    utime.sleep_ms(2000)

utime.sleep_ms(500)
 
print("Fahre los ... Taste L --> stop")

count = 0

    
drehe(V, 5000, RECHTS, s)
'''
while not TASTER_L.value() == 1:
    s.messen()
    diff = s.wertR - s.wertL
    diff = diff * 5
    # utime.sleep_ms(100)
    count = count + 1
    if  count == 20:
        print(s.wertR,s.wertL,diff)
        count = 0

    #OnFwd(MOT_A, V - diff)
    #OnFwd(MOT_B, V + diff)'''
Off(MOT_AB)

  
print("ENDE")