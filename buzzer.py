from machine import Pin, PWM, Timer
from utime import sleep_ms
import math

class Buzzer():
    DUTY_CYCLE=8192
    PI=3.14
    
    notes = {"A0": 28, "A0#": 29, "Bb0": 29, "B0": 31, "C1": 33, "C1#": 35, "Db1": 35, "D1": 37, "D1#": 39, "Eb1": 39, "E1": 41, "F1": 44, "F1#": 46, "Gb1": 46, "G1": 49, "G1#": 52, "Ab1": 52, "A1": 55, "A1#": 58, "Bb1": 58, "B1": 62, "C2": 65, "C2#": 69, "Db2": 69,  "D2": 73, "D2#": 78, "Eb2": 78, "E2": 82, "F2": 87, "F2#": 92, "Gb2": 92, "G2": 98, "G2#": 104, "Ab2": 104, "A2": 110, "A2#": 116, "Bb2": 116, "B2": 124, "C3": 131, "C3#": 139, "Db3": 139, "D3": 147, "D3#": 156, "Eb3": 156, "E3": 165, "F3": 175, "F3#": 185, "Gb3": 185, "G3": 196, "G3#": 208, "Ab3": 208, "A3": 220, "A3#": 233, "Bb3": 233, "B3": 247, "C4": 262, "C4#": 277, "Db4": 277, "D4": 294, "D4#": 311, "Eb4": 311, "E4": 330, "F4": 349, "F4#": 370, "Gb4": 370, "G4": 392, "G4#": 415, "Ab4": 415, "A4": 440, "A4#": 466, "Bb4": 466, "B4": 494, "C5": 523, "C5#": 554, "Db5": 554, "D5": 587, "D5#": 622, "Eb5": 622, "E5": 659, "F5": 698, "F5#": 740, "Gb5": 740, "G5": 784, "G5#": 830.6, "Ab5": 831, "A5": 880, "A5#": 932, "Bb5": 932, "B5": 988, "C6": 1046, "C6#": 1109, "Db6": 1109, "D6": 1175, "D6#": 1244, "Eb6": 1244, "E6": 1318, "F6": 1397, "F6#": 1480, "Gb6": 1480, "G6": 1568, "G6#": 1661, "Ab6": 1661, "A6": 1760, "A6#": 1865, "Bb6": 1865, "B6": 1976, "C7": 2093, "C7#": 2218, "Db7": 2218, "D7": 2349, "D7#": 2489, "Eb7": 2489, "E7": 2637, "F7": 2794, "F7#": 2960, "Gb7": 2960, "G7": 3136, "G7#": 3322, "Ab7": 3322, "A7": 3520, "A7#": 3729, "Bb7": 3729, "B7": 3951, "C8": 4186}
    
    def __init__(self, pin):
        print(pin)
        self.buzzer = PWM(Pin(pin))
        self.buzzer.duty_u16(0)
        self.timer = Timer(-1)
        
    def playNote(self, note, duration=False):
        if note in self.notes:
            self.playFrequency(self.notes[note], duration)
            
    def playFrequency(self, freq, duration=False):
        self.timer.deinit()
        
        if(duration):
            self.timer.init(period=duration, mode=Timer.ONE_SHOT, callback=self.stopPlay)
        self.buzzer.freq(freq)
        self.buzzer.duty_u16(self.DUTY_CYCLE)

    def stopPlay(self, timer=False):
        self.buzzer.duty_u16(0)

    def alert(self, duration=36):
        self.buzzer.duty_u16(self.DUTY_CYCLE)
        
        for x in range(0, duration):
            sinVal  = math.sin(x * 10 * self.PI / 180)
            toneVal = 1500+int(sinVal*500)
            self.buzzer.freq(toneVal)
            sleep_ms(10)

        self.buzzer.duty_u16(0)            