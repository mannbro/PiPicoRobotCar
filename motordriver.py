from machine import Pin, PWM
import utime


class Motordriver():
    OBSTACLE_DETECT_INTERVAL_MS=100
    OBSTACLE_STOP_DISTANCE_MM=100
    
    def __init__(self, buzzer, sonic, leftFwdPin, leftBckPin, leftPWMPin, leftSpdPin, rightFwdPin, rightBckPin, rightPWMPin, rightSpdPin):
        self.buzzer=buzzer
        self.sonic=sonic
        self.leftFwd=Pin(leftFwdPin, Pin.OUT)
        self.leftBck=Pin(leftBckPin, Pin.OUT)
        self.leftPWM=PWM(Pin(leftPWMPin))
        self.leftSpd=Pin(leftSpdPin, Pin.IN) #TODO: Not currently used
        self.rightFwd=Pin(rightFwdPin, Pin.OUT)
        self.rightBck=Pin(rightBckPin, Pin.OUT)
        self.rightPWM=PWM(Pin(rightPWMPin))
        self.rightSpd=Pin(rightSpdPin, Pin.IN) #TODO: Not currently used

    def speedToDuty(self, speed):
        retval = int(speed * 655.35)
        return retval

    def speedToFreq(self, speed):
        retval = int(10+speed)
        return retval


            
    def moveForward(self, speed, duration=False):
        self.buzzer.playFrequency(self.speedToFreq(speed))
        self.leftFwd.value(1)
        self.leftBck.value(0)
        self.leftPWM.duty_u16(self.speedToDuty(speed))

        self.rightFwd.value(1)
        self.rightBck.value(0)
        self.rightPWM.duty_u16(self.speedToDuty(speed))
        
        #TODO: Loop instead of wait,check for collision in loop
        loopStart = utime.ticks_ms()

        while True:
            alert=False
            utime.sleep_ms(self.OBSTACLE_DETECT_INTERVAL_MS)
            distance = self.sonic.getDistanceMm()
            print(distance, "mm")

            #Break on obstacle
            if(distance<self.OBSTACLE_STOP_DISTANCE_MM):
                alert=True
                print("Obstacle Detected: ", distance, "mm")
                break

            if(duration and utime.ticks_ms()>loopStart+duration):
                print("Duration reached")
                break
            
        self.buzzer.stopPlay()
        self.stop()
        
        if(alert):
            self.buzzer.alert(128)

    def moveBackward(self, speed, duration):
        self.buzzer.playFrequency(self.speedToFreq(speed))
        self.leftFwd.value(0)
        self.leftBck.value(1)
        self.leftPWM.duty_u16(self.speedToDuty(speed))

        self.rightFwd.value(0)
        self.rightBck.value(1)
        self.rightPWM.duty_u16(self.speedToDuty(speed))
        
        utime.sleep_ms(duration)
        self.buzzer.stopPlay()
        self.stop()      

    def spinLeft(self, speed, duration):
        self.buzzer.playFrequency(self.speedToFreq(speed)*2)
        self.leftFwd.value(0)
        self.leftBck.value(1)
        self.leftPWM.duty_u16(self.speedToDuty(speed))

        self.rightFwd.value(1)
        self.rightBck.value(0)
        self.rightPWM.duty_u16(self.speedToDuty(speed))
        
        utime.sleep_ms(duration)
        self.buzzer.stopPlay()
        self.stop()      

    def spinRight(self, speed, duration):
        self.buzzer.playFrequency(self.speedToFreq(speed)*2)
        self.buzzer.playNote("C3", 500)
        self.leftFwd.value(1)
        self.leftBck.value(0)
        self.leftPWM.duty_u16(self.speedToDuty(speed))

        self.rightFwd.value(0)
        self.rightBck.value(1)
        self.rightPWM.duty_u16(self.speedToDuty(speed))
        
        utime.sleep_ms(duration)
        self.buzzer.stopPlay()
        self.stop()      


    def stop(self):
        self.buzzer.stopPlay()
        
        self.leftFwd.value(0)
        self.leftBck.value(0)
        self.leftPWM.duty_u16(0)

        self.rightFwd.value(0)
        self.rightBck.value(0)
        self.rightPWM.duty_u16(0)
        
    def test(self, duration):
        print("leftFwd")
        self.leftFwd.value(1)
        utime.sleep_ms(duration)
        self.leftFwd.value(0)
        
        print("leftBck")
        self.leftBck.value(1)
        utime.sleep_ms(duration)
        self.leftBck.value(0)
        
        print("leftPWM")
        self.leftPWM.duty_u16(4096)
        utime.sleep_ms(duration)
        self.leftPWM.duty_u16(0)

        print("rightFwd")
        self.rightFwd.value(1)
        utime.sleep_ms(duration)
        self.rightFwd.value(0)
        
        print("rightBck")
        self.rightBck.value(1)
        utime.sleep_ms(duration)
        self.rightBck.value(0)
        
        print("rightPWM")
        self.rightPWM.duty_u16(4096)
        utime.sleep_ms(duration)
        self.rightPWM.duty_u16(0)

