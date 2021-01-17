import sys
import os
import time
import board
#import Adafruit_DHT
from urllib.request import urlopen
 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
DHT11_SENSOR = Adafruit_DHT.DHT11
DHT11_PIN = 4
TS_KEY = "HVFDZ6711P0WAW4S"
MY_DELAY = 15

IFTTT_KEY = "dmQzjKzewvH4fukMmoBIiJ"



def getSensorData():
    humidity, temperature = Adafruit_DHT.read(DHT11_SENSOR, DHT11_PIN)
    
    # return dict
    return (humidity, temperature)

def sendDataToThingSpeak(temperature, temperature_f, humidity):
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % TS_KEY
    f = urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" % (temperature, temperature_f, humidity))
    #print (f.read())

    f.close()
    time.sleep(int(MY_DELAY))

def sendWebhookToIftt(currentTemp):
    if currentTemp < 70:
        eventName = "fermenton"
    elif currentTemp > 70.8:
        eventName = "fermentoff"
    else:
        print("so warm!")

    if eventName is not None:
        #send event
        Ifttt_url = f'https://maker.ifttt.com/trigger/{eventName}/with/key/{IFTTT_KEY}'
        f = urlopen(Ifttt_url)
        f.close()


def main():
    while True:
        humidity, temperature = getSensorData()
        
        if humidity is not None and temperature is not None:
            # + 33.8 is for calibration based on other temp sensors
            temperature_f = (temperature * 1.8) + 33.8
            sendWebhookToIftt(temperature_f)
            sendDataToThingSpeak(temperature,temperature_f, humidity)
            
        else:
            print("Sensor did not respond");
        time.sleep(10);
    
# call main

if __name__ == "__main__":
    main()