import sys
import os
import time
import board
import Adafruit_DHT
from urllib.request import urlopen
import Ifttt
import thingspeak
 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
airSensor = Adafruit_DHT.DHT11
airSensorPin = 17

kegOneSensor = Adafruit_DHT.DHT22
kegOneSensorPin = 4

kegTwoSensor = Adafruit_DHT.DHT22
kegTwoSensorPin = 27

def getKengOneSensorData():
    return Adafruit_DHT.read_retry(kegOneSensor, kegOneSensorPin)

def getKegTwoSensorData():
    return Adafruit_DHT.read_retry(kegTwoSensor, kegTwoSensorPin)


def getAirSensorData():
    return Adafruit_DHT.read_retry(airSensor, airSensorPin)


def sendWebhookToIftt(currentTemp):
    Ifttt.sendRequest(currentTemp)

def getFahrenheight(celcius):
    return round((celcius * 1.8) + 32, 0)

def main():
    while True:
        kegOne = getKengOneSensorData()
        kegTwo = getKegTwoSensorData()
        air = getAirSensorData()
        
        print("Keg One: " + str(getFahrenheight(kegOne[1])) + "F")
        print("Keg Two: " + str(getFahrenheight(kegTwo[1])) + "F")
        print("Air: " + str(round(air[0], 0)) + "%, " + str(getFahrenheight(air[1])) + "F")
        
        thingspeak.sendDataToThingSpeak(kegOne,kegTwo,air)
        Ifttt.sendRequest(getFahrenheight(kegOne[1]))
    
# call main

if __name__ == "__main__":
    main()