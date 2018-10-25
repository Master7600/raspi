#Toggle LED with Button Program
#Connect the LED to GPIO 22 Pin and Button to GPIO 5 Pin

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

ledPin = 22
buttonPin = 5

#setup the ledPin(i.e. GPIO22) as output and buttonPin(i.e. GPIO5) as input
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, False)

buttonPress = True
ledState = False

try:
    while True:
        print("Press the Button!")
        buttonPress = GPIO.input(buttonPin)
        if buttonPress == False and ledState == False:
            GPIO.output(ledPin, True)
            print("LED ON")
            ledState = True
            sleep(0.5)
        elif buttonPress == False and ledState == True:
            GPIO.output(ledPin, False)
            print("LED OFF")
            ledState = False
            sleep(0.5)
        sleep(0.1)        
finally:
    #reset the GPIO Pins
    GPIO.output(ledPin, False)
    GPIO.cleanup()
    


