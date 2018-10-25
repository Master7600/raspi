import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 35    # Input Pin
Motor2 = 37    # Input Pin

 
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
try:
    while True:
        print "FORWARD MOTION"
        GPIO.output(Motor1,GPIO.HIGH)
        GPIO.output(Motor2,GPIO.LOW)
        sleep(1)
     
    #print "BACKWARD MOTION"
    #GPIO.output(Motor1,GPIO.LOW)
    #GPIO.output(Motor2,GPIO.HIGH)

 
#sleep(3)
 

finally:
    #reset the GPIO Pins
    GPIO.cleanup()
