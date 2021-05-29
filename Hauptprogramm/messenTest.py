import utime
import machine
from sensor_licht import *
from motor import *

LEDW = 18
LEDR = 19
LEDG = 20

def kalibrieren(sensoren,anzahl=500):
    #die Sensoren werden als Tupel übergeben
    n = 0
    for i in range(anzahl):
        for s in sensoren:
            s.kalibrierRunde()
            utime.sleep(0.01)

if __name__=="__main__":
    s1=Sensor(LEDW)
    s2=Sensor(LEDR)
    s3=Sensor(LEDG)
    sensoren=(s1,s2,s3)
    print("Kalibrieren")
    kalibrieren(sensoren)
    print("Kalibrieren fertig!")
    
    i=0
    for s in sensoren:
        i+=1
    #ini,maxi=s.getMinMax()    
   #     print("Sensor",str(i)," ", str(mini)," ",str(maxi))
   # utime.sleep(2)
    while True:
        s1.messen()
        print(s1.wertL, s1.wertR)
        utime.sleep(0.4)
    
    