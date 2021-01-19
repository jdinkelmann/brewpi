import time
from urllib.request import urlopen


class Thingspeak():
    TS_KEY = "HVFDZ6711P0WAW4S"
    MY_DELAY = 15

    
    def __init__(self, *args, **kwargs):
        super(Thingspeak, self).__init__(*args, **kwargs)

def getFahrenheight(celcius):
    return round((celcius * 1.8) + 32, 0)

def sendDataToThingSpeak(kegOne, kegTwo, air):
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % Thingspeak.TS_KEY
    
    f1 = kegOne[0]
    f2 = getFahrenheight(kegOne[1])
    f3 = kegTwo[0]
    f4 = getFahrenheight(kegTwo[1])
    f5 = air[0]
    f6 = getFahrenheight(air[1])
    
    f = urlopen(baseURL + "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s" % (f1, f2, f3, f4, f5, f6))
    #print (f.read())

    f.close()
    time.sleep(int(Thingspeak.MY_DELAY))