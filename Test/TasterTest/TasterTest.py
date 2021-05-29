import machine

TASTER_L = machine.Pin(16 , machine.Pin.IN)
TASTER_R = machine.Pin(17 , machine.Pin.IN)

if TASTER_L.value() :
    print("L")
    print("")