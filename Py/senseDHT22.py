import pigpio
import DHT22
from time import sleep

#Initiate GPIO for pigpio
pi = pigpio.pi()

#Setup the sensor
dht22 = DHT22.sensor(pi, 27) #use the actual GPIO Pin name
dht22.trigger()

#Sleep time must be above 3 seconds
sleepTime = 3

def readDHT22():
    #get new reading
    dht22.trigger()
    #save our value
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return (humidity, temp)

while True:
    humidity, temperature = readDHT22()
    print("Humidity is: "+ humidity + "%")
    print("Temperature is: " + temperature + "C")
    sleep(sleepTime)
