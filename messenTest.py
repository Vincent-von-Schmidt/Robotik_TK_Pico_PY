import utime
import machine
from sensor import *
SENSOR_1_PIN= 26
SENSOR_2_PIN= 27



def kalibrieren(sensoren,anzahl=500):
    #die Sensoren werden als Tupel übergeben
    n = 0
    for i in range(anzahl):
        for s in sensoren:
            s.kalibrierRunde()
            utime.sleep(0.01)

if __name__=="__main__":
    s1=Sensor(SENSOR_1_PIN)
    s2=Sensor(SENSOR_2_PIN)
    sensoren=(s1,s2)
    print("Kalibrieren")
    kalibrieren(sensoren)
    
    i=0
    for s in sensoren:
        i+=1
        mini,maxi=s.getMinMax()    
        print("Sensor",str(i)," ", str(mini)," ",str(maxi))
    utime.sleep(2)
    while True:
        print (str(s1.messen())," ",str(s2.messen()))
        utime.sleep(0.4)
    
    