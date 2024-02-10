#Tutorial: 
    #PiMyLifeUp 
    #https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ 

 
#import module for time and date
import Adafruit_DHT 
from datetime import datetime 

 
#define sensor and pins
DHT_SENSOR = Adafruit_DHT.DHT22 
DHT_PIN = 4 


while True: 

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) 
    #if humidity and temperature is known 

    if humidity is not None and temperature is not None: 

        #program opens file
        with open('humidity.txt', "a") as data: 


            #writes parameters and timestamp
            data.write("Date and time: {0} Temperature: {1:0.1f}*C  Humidity: {2:0.1f}% \n".format(datetime.now(), temperature, humidity)) 


            #closes file
            data.close() 

             
    else: 

        print("ERROR: No temperature or humidity data could be obtained") 