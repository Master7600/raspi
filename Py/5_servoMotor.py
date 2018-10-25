# Controlling servo motor with PWM

import RPi.GPIO as GPIO     #mport libraries
import time

GPIO.setmode(GPIO.BCM)      # using BCM mode for numbering the pins, you can also use BOARD mode

servoPin = 17               #using GPIO17 pin for signalling servo

GPIO.setup(servoPin, GPIO.OUT)  #set GPIO17 pin as output
pwm = GPIO.PWM(servoPin, 50)   # setting up channel and frequency for servo (f = 50hz for servo)
pwm.start(0)                # provide the duty cycle

try:
    while 1:
        for i in range(0, 180, 1):
            dutycycleVal = 1/18. * (i) + 2 # formula (y2 - y1) = m(x2 - x1)
            pwm.ChangeDutyCycle(dutycycleVal)
            time.sleep(0.01)
        for i in range(180, 0, -1):
            dutycycleVal = 1/18. * (i) + 2
            pwm.ChangeDutyCycle(dutycycleVal)
            time.sleep(0.01)
finally:
    pwm.stop()
    GPIO.cleanup()
