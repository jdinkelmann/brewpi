from urllib.request import urlopen

class Ifttt():
    IFTTT_KEY = "dmQzjKzewvH4fukMmoBIiJ"
    LAST_EVENT = ""

    def __init__(self, *args, **kwargs):
        super(Ifttt, self).__init__(*args, **kwargs)


def checkTemperature(currentTemp):
    if currentTemp < 70:
        eventName = "fermenton"
    elif currentTemp > 70.8:
        eventName = "fermentoff"
    else:
        eventName = ""
        #print("so warm!")

    return eventName

def sendRequest(currentTemp):
    currentTempEvent = checkTemperature(currentTemp)

    if currentTemp is not None:
        Ifttt_url = f'https://maker.ifttt.com/trigger/{currentTempEvent}/with/key/{IFTTT_KEY}'
        f = urlopen(Ifttt_url)
        f.close()
