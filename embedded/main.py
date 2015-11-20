#!/usr/bin/env python

"""
Module for handling embedded application
"""

import RPi.GPIO as GPIO
import time

import logger
import database
import nfc

GREEN_LED = 16
RED_LED = 18

LED_BLINK_TIME = 0.1
SYS_PAUSE_TIME = 2

def ledOn(led):
    GPIO.output(led, GPIO.HIGH)

def ledOff(led):
    GPIO.output(led, GPIO.LOW)

def blinkLed(led):
    for i in range(0, 3):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(LED_BLINK_TIME)
        GPIO.output(led, GPIO.LOW)
        time.sleep(LED_BLINK_TIME)

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

def main():
    logger.setupLogger()
    logger.info("Starting application")

    db = database.Database()
    db.createConnection()

    try:
        initGpio()
        while True:
            tagId = nfc.readNfc()
            employeeId = db.getEmployeeIdFromTagId(tagId)
            if (employeeId != None):
                logger.info("Employee authorized")
                db.addNewTimestampOfEmployeeId(employeeId)
                blinkLed(GREEN_LED)
                time.sleep(SYS_PAUSE_TIME)
            else:
                logger.info("Employee NOT authorized")
                blinkLed(RED_LED)
                time.sleep(SYS_PAUSE_TIME)

    except KeyboardInterrupt:
        logger.info("Closing application")
        GPIO.cleanup()
        db.closeConnection()

if __name__ == '__main__':
    main()
