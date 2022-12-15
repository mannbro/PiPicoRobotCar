from utime import sleep_ms, sleep
import random

from ultrasonic import Ultrasonic
from motordriver import Motordriver
from buzzer import Buzzer

buzPin=15
buzzer=Buzzer(buzPin)

trigPin=19
echoPin=18
sonic=Ultrasonic(trigPin, echoPin)

leftFwdPin=10
leftBckPin=11
leftPWMPin=5
leftSpdPin=26
rightFwdPin=12
rightBckPin=13
rightPWMPin=3
rightSpdPin=27
motor=Motordriver(buzzer, sonic, leftFwdPin, leftBckPin, leftPWMPin, leftSpdPin, rightFwdPin, rightBckPin, rightPWMPin, rightSpdPin)



def autonomousDrive(speed):
    while True:
        print("Moving Forward until Obstacle Detected")
        motor.moveForward(speed, False)
        print("Oops!")
        sleep_ms(400)
        print("Backing up slightly...")
        motor.moveBackward(int(speed/2), 600)
        sleep_ms(400)
        print("Turning Randomly")
        if(random.random()>0.5):
            print("Spinning left")
            motor.spinLeft(int(speed/2), int(400+(random.random()*400)))
        else:
            print("Spinning right")
            motor.spinRight(int(speed/2), int(200+(random.random()*300)))
            
        sleep_ms(200)
            