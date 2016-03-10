'''
Created on 10.3.2016

@author: jhofman
'''

import requests
import urllib
import json
import time
urlbase='http://192.168.4.1/console/send?text='
session = requests.Session()
session.trust_env = False

FRONT_LIGHTS = 13
RIGHT_LIGHT = 11
LEFT_LIGHT = 12

def wait(s):
    time.sleep(s)

def getCommand(what, data):
    dataKey = "mdata" if what=="drive" else "data"
    
    command = {"command":what, dataKey:data}
    return command


def getUrl(command):
    url = urlbase + urllib.parse.quote(json.dumps(command))+'%0D%0A'
    return url

def sendCommand(command):
    url = getUrl(command)
    r = session.post(url+'%0D%0A', data = {})
    print(r)


def lightsOn(light, blink):
    sendCommand(getCommand("light", [light, 1, blink]))
def lightsOff(light):
    sendCommand(getCommand("light", [light, 0 , 0]))

def goForward(time=None, speed=None):
    if time is None:
        time = 1000
    if speed is None:
        speed = 150
    return sendCommand(getCommand("drive", [1, speed, time]))

def goBackward(time=None, speed=None):
    if time is None:
        time = 1000
    if speed is None:
        speed = 150
    return sendCommand(getCommand("drive", [2, speed, time]))

def turnRight(time=None, speed=None):
    if time is None:
        time = 1000
    if speed is None:
        speed = 150
    return sendCommand(getCommand("drive", [3, speed, time]))

def turnLeft(time=None, speed=None):
    if time is None:
        time = 1000
    if speed is None:
        speed = 150
    return sendCommand(getCommand("drive", [4, speed, time]))

def allLightsOff():
    lightsOff(FRONT_LIGHTS)
    lightsOff(LEFT_LIGHT)
    lightsOff(RIGHT_LIGHT)
    

if __name__ == '__main__':
    print("Ahoj")

    allLightsOff()
    
    lightsOn(FRONT_LIGHTS, 0)
    goForward()
    lightsOff(FRONT_LIGHTS)
    wait(1)
    lightsOn(LEFT_LIGHT, 100)
    turnLeft()
    lightsOff(LEFT_LIGHT)
    goBackward()
    
