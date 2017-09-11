# -*- coding: utf-8 -*-
'''

'''
import requests
import csv
import time

import datetime

FIRST_ATTR = 'sensorLastObservations'
NUM_OF_OBJ = 0

MIN_FIFTEEN = 900000


def save2csv(fileName, listoflists):
    with open(fileName, 'a+') as csvfile:
        csvwriter = csv.writer(csvfile)
        for l in listoflists:
            csvwriter.writerow(l)
    return


def getDataSensorAtSpecificTime(sensor, debug, timestampFrom, timestampTo):
    '''
    sensor: the id of the sensors
    '''
    timestamp =int(time.time()*1000)
    print [timestamp]

    fromFormatted = datetime.datetime.fromtimestamp(timestampFrom/1000.0).strftime('%d/%m/%YT%H:%M:%S')
    toFormatted = datetime.datetime.fromtimestamp(timestampTo/1000.0).strftime('%d/%m/%YT%H:%M:%S')

    url = 'http://sentilo.bcn.cat/connecta-catalog-web/component/map/%s/lastOb/?from=%s&to=%s' %(sensor,fromFormatted,toFormatted)
    print (url)

    r = requests.get(url)
    if r.status_code==200:
        s = r.json()
        if debug is True:
            print s
        data = [
         s[FIRST_ATTR][NUM_OF_OBJ]['sensor'],
         s[FIRST_ATTR][NUM_OF_OBJ]['sensorState'],
         s[FIRST_ATTR][NUM_OF_OBJ]['value'],
         s[FIRST_ATTR][NUM_OF_OBJ]['unit'],
         s[FIRST_ATTR][NUM_OF_OBJ]['timestamp']]

        save2csv('sensorsData.csv', [data])
    else:
        return None

    return

def getDataFromTo(listOfSensors, fromMillis, toMillis, debug):
    numOfEntries = 0
    while (fromMillis <= toMillis):         #and numOfEntries < 6
        toInterval = fromMillis + MIN_FIFTEEN
        for sensor in listOfSensors:
            numOfEntries += 1
            getDataSensorAtSpecificTime(sensor, debug, fromMillis, toInterval)
        fromMillis += MIN_FIFTEEN        #5 min interval

    print ('Finished parsing sensors. Parsed %s entries' %(numOfEntries))


if __name__ == "__main__":

    #List of sensors in passeig de Gracia
    listofsensors=['CESVA.TA120-T240424', 'CESVA.TA120-T240425', 'CESVA.TA120-T240426', 'CESVA.TA120-T240427']

    #From: Mon Sep 11 2017 06:30:00 GMT+0200
    #To: Mon Sep 11 2017 20:00:00 GMT+0200
    getDataFromTo(listofsensors, 1505104200000, 1505152800000, True)
