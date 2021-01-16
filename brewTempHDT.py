import sys
import os
import time
import board
import Adafruit_DHT
from urllib.request import urlopen
 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
myAPI = "HVFDZ6711P0WAW4S"
MY_DELAY = 15

IS_KEY = "ist_vpgVcIHaPWXqH2NsA3-HdXd2uy3Tg9oY"
IS_BUCKET_KEY = "SNS9MBQYJ4UE"

def getSensorData():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    # return dict
    return (humidity, temperature)

def sendData(temperature, temperature_f, humidity):
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    iSBaseURL = f'https://groker.init.st/api/events?accessKey={IS_KEY}&bucketKey={IS_BUCKET_KEY}'
    
    f = urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" % (temperature, temperature_f, humidity))
    print (f.read())
    
    inState = urlopen(iSBaseURL + "&humidity=%s&ahrenheit=%s&celsius=%s" % (humidity,temperature_f, temperature))
    print (inState.read())
    #print ("tempC " + str(temperature) + ",  " + str(temperature_f) + ", humidity " + str(humidity))
    
    f.close()
    time.sleep(int(MY_DELAY))
    

def main():
    while True:
        humidity, temperature = getSensorData()
        
        if humidity is not None and temperature is not None:
        #print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
            temperature_f = (temperature * 1.8) + 32
            print(humidity)
            print(temperature)
            print(temperature_f)
            sendData(temperature,temperature_f, humidity)
            
        else:
            print("Sensor failure. Check wiring.");
        time.sleep(5);
    
# call main

if __name__ == "__main__":
    main()