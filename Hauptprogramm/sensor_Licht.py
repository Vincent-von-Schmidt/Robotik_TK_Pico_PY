import machine
import utime


SENSOR_R = 26
SENSOR_L = 27


class Sensor:
    def __init__(self, LED, name = "TestSensor", SENSOR_RECHTS = SENSOR_R, SENSOR_LINKS = SENSOR_L):
        """
        Initialisierung
        """
        self.pinR = machine.ADC(SENSOR_RECHTS)
        self.pinL = machine.ADC(SENSOR_LINKS)
        self.led = machine.Pin(LED , machine.Pin.OUT)
        self.wertL = 0
        self.wertR = 0
        self.name = name
        self.maxiL = 0
        self.miniL = 65536
        self.maxiR = 0
        self.miniR = 65536
        
    def kalibrierStart(self):
        """
        Reset der Max/Minvariablen
        """
        self.maxiL = 0
        self.miniL = 65536
        self.maxiR = 0
        self.miniR = 65536
        
    def kalibrierRunde(self):
        """
        misst und setzt bei Bedarf Minimum und Maximum
        """
        self.led.value(1)
        utime.sleep_us(30)
        self.wertR = self.pinR.read_u16()
        self.wertL = self.pinL.read_u16()
        #print("messe", self.name)
        self.led.value(0)
        if self.wertL > self.maxiL:
            self.maxiL = self.wertL
        if self.wertL < self.miniL:
            self.miniL = self.wertL
        if self.wertR > self.maxiR:
            self.maxiR = self.wertR
        if self.wertR < self.miniR:
            self.miniR = self.wertR

    def map2int(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
        
    def messen(self):
        self.led.value(1)
        utime.sleep_us(30)
        wertR = self.pinR.read_u16()
        wertL = self.pinL.read_u16()
        #print("messe", self.name)
        self.led.value(0)
        self.wertL = self.map2int(wertL, self.miniL, self.maxiL, 0, 100)
        self.wertR = self.map2int(wertR, self.miniR, self.maxiR, 0, 100)
        
    def setMinMax(self, minL, maxL, minR, maxR):
        self.maxiL = maxL
        self.miniL = minL
        self.maxiR = maxR
        self.miniR = minR
        
    def printMinMax(self):
        print("minL = " + str(self.miniL))
        print("maxL = " + str(self.maxiL))
        print("minR = " + str(self.miniR))
        print("maxL = " + str(self.maxiR))
         
         