#Blink LED Program
#Connect the LED to GPIO 22 Pin
#LED Blink Progarm
#Connect the LED to GPIO22 (i.e. Physical Pin15)


#import GPIO and time library
import RPi.GPIO as GPIO     
from time import sleep

GPIO.setmode(GPIO.BCM)   #set the Pin mode you will be working with

ledPin = 22   #this is GPIO22 pin i.e Physical Pin15

#setup the ledPin(i.e. GPIO22) as output
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)   #Set the LED Pin to HIGH
        print("LED ON")
        sleep(1)                    #Wait for 1 sec
        GPIO.output(ledPin, False)  #Set the LED Pin to LOW
        print("LED OFF")
        sleep(1)                    #wait for 1 sec
finally:
    #reset the GPIO Pins
    GPIO.output(ledPin, False)
    GPIO.cleanup()
    


