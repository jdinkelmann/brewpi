from urllib.request import urlopen

class Ifttt():
    IFTTT_KEY = "dmQzjKzewvH4fukMmoBIiJ"
    LAST_EVENT = ""
    MIN_TEMP = 69
    MAX_TEMP = 71

    def __init__(self, *args, **kwargs):
        super(Ifttt, self).__init__(*args, **kwargs)


def checkTemperature(currentTemp):
    #print("Current Temp: " + str(currentTemp) + "F")
    
    if currentTemp < 69:
        eventName = "fermenton"
    elif currentTemp > 71:
        eventName = "fermentoff"
    else:
        eventName = ""
        #print("so warm!")

    return eventName

def sendRequest(currentTemp):
    currentTempEvent = checkTemperature(currentTemp)
    
    if currentTemp is not None:
        if Ifttt.LAST_EVENT is not currentTempEvent:
            Ifttt.LAST_EVENT = currentTempEvent
            print("calling webhook")
            Ifttt_url = f'https://maker.ifttt.com/trigger/{currentTempEvent}/with/key/dmQzjKzewvH4fukMmoBIiJ'
            f = urlopen(Ifttt_url)
            print(f.read())
            f.close()
