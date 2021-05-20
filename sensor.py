import machine

class Sensor:
    def __init__(self,pin):
        """
        Initialisierung
        """
        self.pin= machine.ADC(pin)
        self.maxi= 0
        self.mini= 65535
        
    def setMinMax(self,mini,maxi):
        """
        setzt die Kalibrierwerte
        """
        self.mini=mini
        self.maxi=maxi
    
    def getMinMax(self):
        """
        liefert ein Tupel (min, max)
        """
        return self.mini,self.maxi
    
    def kalibrierRunde(self):
        """
        setzt bei Bedarf Minimum und Maximum
        """
        wert=self.pin.read_u16()
        if wert>self.maxi:
            self.maxi = wert
        if wert<self.mini:
            self.mini = wert
            
    def messen(self):
        """
        liefert den kalibrierten Wert
        """
        wert=self.pin.read_u16()        
        return (wert - self.mini) * 100 // (self.maxi - self.mini)

        
        