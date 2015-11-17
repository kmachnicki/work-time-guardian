#!/usr/bin/env python

"""
Module for handling RFID
"""

import time
import psycopg2

def createDbConnection():
    return psycopg2.connect("dbname=wbudowane user=wbudowane password=alamakota")

def addNewTimestampToDb(dbConnection, employeeId):
    timestamp = psycopg2.TimestampFromTicks(int(time.time()))
    cursor = dbConnection.cursor()
    cursor.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) VALUES (%s, %s);", employeeId, timestamp)
    cursor.commit()

def main():
    dbConnection = createDbConnection()

    #addNewTimestampToDb(dbConnection, employeeId)

if __name__=='__main__':
    main()
