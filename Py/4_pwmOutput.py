import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pwmPin = 17
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 100)

pwm.start(0)

try:    
    while 1:
        dutyCycleVal = input("Enter the brightness between 1% to 100%; ")
        pwm.ChangeDutyCycle(float(dutyCycleVal))
        time.sleep(0.1)
        
finally:
    pwm.stop()
    GPIO.cleanup()


