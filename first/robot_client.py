import requests
import telnetlib

host = '192.168.4.1'
url_prefix = 'http://' + host + '/console/send?text='
url_light_on = url_prefix + '%7B%22command%22%3A%22lights%22%2C%22data%22%3A%5B12%2C1%2C0%5D%7D%0D%0A'
url_light_off = url_prefix + '%7B%22command%22%3A%22lights%22%2C%22data%22%3A%5B12%2C%2C%5D%7D%0D%0A'

tn = telnetlib.Telnet(host, port=23)
distance = ""

maxDistanceFromWall = 14
minDistanceFromWall = 6

def goForward( speed, drivingPeriod ):
    print "go forward: " + str(speed) + " : " + str(drivingPeriod)
    response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B1%2C' + str(speed) + '%2C' + str(drivingPeriod) + '%5D%7D%0D%0A')
    print response

def goBackward( speed, drivingPeriod ):
    print "go backward: " + str(speed) + " : " + str(drivingPeriod)
    response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B2%2C' + str(speed) + '%2C' + str(drivingPeriod) + '%5D%7D%0D%0A')
    print response

def turnRight( speed, drivingPeriod ):
    print "turn right: " + str(speed) + " : " + str(drivingPeriod)
    response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B3%2C' + str(speed) + '%2C' + str(drivingPeriod) + '%5D%7D%0D%0A')
    print response

def turnLeft( speed, drivingPeriod ):
    print "turn left: " + str(speed) + " : " + str(drivingPeriod)
    response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B4%2C' + str(speed) + '%2C' + str(drivingPeriod) + '%5D%7D%0D%0A')
    print response

# def turn90DecToRight():
#     print "turn 90 dec to right"
#     response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B3%2C' + str(100) + '%2C' + str(400) + '%5D%7D%0D%0A')
#     print response
#
# def turn90DecToLeft():
#     print "turn 90 dec to right"
#     response = requests.post(url_prefix + '%7B%22command%22%3A%22drive%22%2C%22mdata%22%3A%5B4%2C' + str(100) + '%2C' + str(400) + '%5D%7D%0D%0A')
#     print response

while True:
    # data = tn.read_until("string that is not going to be found", timeout=0.5)
    # if data:
    #     distance = data[data.find("[", data.find("distance")):len(data)][1:data[data.find("[", data.find("distance")):len(data)].find("]")]
    #     if distance:
    #         print "DISTANCE = " + distance
    #         if int(distance) > maxDistanceFromWall:
    #             rigthTurnDone = False
    #             goForward(125, 175)
    #         elif int(distance) < minDistanceFromWall:
    #               goBackward(125, 175)
    #         else:
    #             if not rigthTurnDone:
    #                 rigthTurnDone = True
    #                 turn90DecToRight()
    #             else:
    #                 turn90DecToLeft()

    data = tn.read_until("string that is not going to be found", timeout=1)
    if data:
        edge = data[data.find("[", data.find("edge")):len(data)][1:data[data.find("[", data.find("edge")):len(data)].find("]")]
        if edge:
            print "EDGE = " + edge

            if "1,1" in edge:
                goForward(100, 100)
            elif "0,1" in edge:
                turnLeft( 100, 100 )
            elif "1,0" in edge:
                turnRight( 100, 100 )
            if "0,0" in edge:
               turnRight( 100, 100 )
