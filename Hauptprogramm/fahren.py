import utime
from motor import *

SCHWARZ = 60
RECHTS = 0
LINKS = 1

def drehe(V, t, richtung, sensor):
    t1 = utime.ticks_ms()
    t2 = t1
    Mot1 = MOT_A
    Mot2 = MOT_B
    if richtung == LINKS:
        Mot1 = MOT_B
        Mot2 = MOT_A
    OnFwd(Mot2, V) #drehen
    OnRev(Mot1, V)
    while ((t2 - t1) < t):
        utime.sleep_ms(1)
        sensor.messen()
        t2 = utime.ticks_ms()
        if richtung == RECHTS:
            SensorWert = sensor.wertR
        else:
            SensorWert = sensor.wertL
        if SensorWert < SCHWARZ:
            Off(MOT_AB)
            return 1 # schwarz gefunden -> stop und return
    Off(MOT_AB)
    return 0

def fahreVor(V, t, sensor, richtung):
    t1 = utime.ticks_ms
    t2 = t1

    OnFwd(MOT_AB, V)

    while (t2 - t1) < t:
        utime.sleep_ms(1)
        sensor.messen()
        t2 = utime.ticks_ms()
        if richtung == RECHTS:
            SensorWert = sensor.wertR
        else:
            SensorWert = sensor.wertL
        if SensorWert < SCHWARZ: 
            Off(MOT_AB)
            return 1 # schwarz gefunden -> stop und return
        
        Off(MOT_AB) 
        return 0



def doseUmfahren(richtung, sensor):
    Mot1 = MOT_A
    Mot2 = MOT_B
    if richtung == RECHTS:
        Mot1 = MOT_B
        Mot2 = MOT_A
    OnRev(MOT_AB, 60)
    utime.sleep(1)
    Off(MOT_AB)
    OnFwd(Mot1, 80)
    OnFwd(Mot2, 80)
    utime.sleep(1)
    Off(MOT_AB)
    utime.sleep_ms(1500)
    
    istSchwarz = 1
    while istSchwarz == 0:
        print(istSchwarz)
        istSchwarz = drehe(100, 400, richtung, sensor)
        if istSchwarz == 0:
            istSchwarz = fahreVor(80, 700, sensor, richtung)
    
    OnFwd(Mot1, 120)
    OnRev(Mot2, 50)
    utime.sleep_ms(500)
    OnFwd(MOT_AB, 80)
    utime.sleep_ms(500)
    
    if richtung == RECHTS:
        drehe(100, 2000, LINKS)
    else:
        drehe(100, 2000, RECHTS)
    Off(MOT_AB)