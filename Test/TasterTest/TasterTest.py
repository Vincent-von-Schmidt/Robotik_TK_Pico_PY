import machine
import utime


TASTER_L = machine.Pin(16 , machine.Pin.IN, machine.Pin.PULL_DOWN)
TASTER_R = machine.Pin(17 , machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print(TASTER_L.value())
    utime.sleep_ms(200)