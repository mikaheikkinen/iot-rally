'''
Created on 10.3.2016

@author: jhofman
'''

import requests
import urllib
import json
import time

import msvcrt

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
    return r

def lightsOn(light, blink):
    sendCommand(getCommand("light", [light, 1, blink]))
def lightsOff(light):
    sendCommand(getCommand("light", [light, 0 , 0]))

def goForward(time=None, speed=None):
    if time is None:
        time = 100
    if speed is None:
        speed = 150
    #lightsOn(FRONT_LIGHTS, 0)
    sendCommand(getCommand("drive", [1, speed, time]))
    #lightsOff(FRONT_LIGHTS)

def goBackward(time=None, speed=None):
    if time is None:
        time = 100
    if speed is None:
        speed = 150
    sendCommand(getCommand("drive", [2, speed, time]))

def turnRight(time=None, speed=None):
    if time is None:
        time = 100
    if speed is None:
        speed = 100
    #lightsOn(RIGHT_LIGHT, 100)
    sendCommand(getCommand("drive", [3, speed, time]))
    #lightsOff(RIGHT_LIGHT)

def turnLeft(time=None, speed=None):
    if time is None:
        time = 100
    if speed is None:
        speed = 100
    #lightsOn(LEFT_LIGHT, 100)
    sendCommand(getCommand("drive", [4, speed, time]))
    #lightsOff(LEFT_LIGHT)


def allLightsOff():
    lightsOff(FRONT_LIGHTS)
    lightsOff(LEFT_LIGHT)
    lightsOff(RIGHT_LIGHT)


if __name__ == '__main__':
    allLightsOff()

    while True:
        key = ord(msvcrt.getch())
        if key==72:
            goForward()
        if key==77:
            turnRight()
        if key==80:
            goBackward()
        if key==75:
            turnLeft()
        if key==13:
            break
