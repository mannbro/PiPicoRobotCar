from machine import Pin
import utime

class Ultrasonic():
    SOUND_VELOCITY = 340
    def __init__(self, trigPin, echoPin):
        self.trig=Pin(trigPin, Pin.OUT, 0)
        self.echo=Pin(echoPin, Pin.IN, 0)

    def getDistanceMm(self):
        self.trig.value(1)
        utime.sleep_us(10)
        self.trig.value(0)
        while not self.echo.value():
            pass

        pingStart = utime.ticks_us()

        while self.echo.value():
            pass
        
        pingStop = utime.ticks_us()
        distanceTime = utime.ticks_diff(pingStop, pingStart) // 2
        mm = int(self.SOUND_VELOCITY * distanceTime // 1000)
        
        return mm

    
