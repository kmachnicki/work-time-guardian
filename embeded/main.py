#!/usr/bin/env python

"""
Module for handling embedded application
"""

import RPi.GPIO as GPIO
import logging
import time

import database
import nfc

GREEN_LED = 16
RED_RED = 18

def ledOn(led):
    GPIO.output(led, GPIO.HIGH)

def ledOff(led):
    GPIO.output(led, GPIO.LOW)

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_RED, GPIO.OUT)

def main():
    database = Database()
    database.createConnection()

    GPIO.cleanup()

    try:
        initGpio()
        while True:
            tagId = nfc.readNfc()
            employeeId = getEmployeeIdFromTagId(tagId)
            if (employeeId != None):
                database.addNewTimestampOfEmployeeId(employeeId)
                ledOn(GREEN_LED)
                time.sleep(3)
                ledOff(GREEN_LED)
            else:
                ledOn(RED_RED)
                time.sleep(3)
                ledOff(RED_RED)

    except KeyboardInterrupt:
        logging.info("Closing application")
        GPIO.cleanup()
        database.closeConnection()

if __name__ == '__main__':
    main()
