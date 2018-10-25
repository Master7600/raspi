#Toggle REALY with Button Program
#Connect the RELAY to GPIO 22 Pin and Button to GPIO 5 Pin

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

maxCount = 4
count = 0
relayPin = 22
buttonPin = 5

#setup the ledPin(i.e. GPIO22) as output and buttonPin(i.e. GPIO5) as input
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(relayPin, False)

buttonPress = True
relayState = False

try:
    while count < maxCount:
        print("Press the Button!")
        buttonPress = GPIO.input(buttonPin)
        if buttonPress == False and relayState == False:
            GPIO.output(relayPin, True)
            print("Relay ON")
            relayState = True
            sleep(0.5)
        elif buttonPress == False and relayState == True:
            GPIO.output(relayPin, False)
            print("Relay OFF")
            relayState = False
            count += 1
            sleep(0.5)
        sleep(0.1)
        
finally:
    #reset the GPIO Pins
    GPIO.output(relayPin, False)
    GPIO.cleanup()
    


