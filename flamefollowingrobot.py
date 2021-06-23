#Flame Following Robot using Raspberry Pi Pico and MicroPython
#Author: MohammadReza Sharifi

from machine import Pin as pin

#Define Flame Sensors pins
middleSensor = pin(15,pin.IN)
rightSensor = pin(14,pin.IN)
leftSensor = pin(13,pin.IN)

#Define Driver pins
in1 = pin(16,pin.OUT)
in2 = pin(17,pin.OUT)
in3 = pin(18,pin.OUT)
in4 = pin(19,pin.OUT)

#########
ENA = pin(20,pin.OUT)
ENB = pin(21,pin.OUT)

ENA.value(1)
ENB.value(1)
#########

#Defien Alarm pins
buzzer = pin(11,pin.OUT)
led = pin(12,pin.OUT)

#This Function moves the Robot forward
def forward():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    buzzer.value(1)
    led.value(1)

#This Function moves the Robot backward
def backward():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)
    buzzer.value(1)
    led.value(1)
    
#This Function moves the Robot right
def right():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    buzzer.value(1)
    led.value(1)

#This Function moves the Robot left
def left():
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    buzzer.value(1)
    led.value(1)

#This Function stops the Robot
def stopfcn():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    buzzer.value(0)
    led.value(0)

while True:
    #Read Digital value from Flame Sensors
    middleDetector = middleSensor.value()
    rightDetector = rightSensor.value()
    leftDetector = leftSensor.value()
    
    if middleDetector == False and rightDetector == False and leftDetector == False:
        forward()
        #print("forward is OK!")
        
    elif middleDetector == True and rightDetector == True and leftDetector == False:
        right()
        #print("right is OK!")
    
    elif middleDetector == True and rightDetector == False and leftDetector == True:
        left()
        #print("left is OK!")
        
    elif middleDetector == True and rightDetector == False and leftDetector == False:
        stopfcn()
        #print("robot has been stopped")
        
    else:
        pass
        
        
#print commands in while loop are for testing conditions
#middle flame sensor is low active
#other sensors are high active
