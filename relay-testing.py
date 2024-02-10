#Tutorial: 
    #Explaning Computers 
    #Raspberry Pi Automation #1: Mains Relay HAT 
    #https://www.youtube.com/watch?v=bOGltcgiXiU 


import RPi.GPIO as GPIO 
import time 


#setting up pins
GPIO.setmode(GPIO.BCM) 
GPIO.setup(9, GPIO.OUT) #GROUND pin 
GPIO.setup(17, GPIO.OUT) #3.3 VCD POWER pin 
GPIO.setup(11, GPIO.OUT) #GPIO 0 pin 


try: 

        while True: 

 
                #pin 11 has signal, waits for 3 sec
                GPIO.output(11, True) 
                time.sleep(3) 

                
                #pin 11: no signal, pin 9: has signal, waits for 3 sec
                GPIO.output(11, False) 
                GPIO.output(9, True) 
                time.sleep(3) 

                 
                #pin 9: no signal, pin 17 has signal, waits for 3 sec 
                GPIO.output(9, False) 
                GPIO.output(17, True) 
                time.sleep(3) 

                 
                #pin 17: no signal
                GPIO.output(17, False) 

 
finally: 

        #pin cleanup
        GPIO.cleanup() 
        print("Konec programa") 