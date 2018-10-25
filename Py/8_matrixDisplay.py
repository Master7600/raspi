import max7219.led as led


device = led.matrix() #cascaded = 3
while 1:
    device.show_message("Edkits")

    
