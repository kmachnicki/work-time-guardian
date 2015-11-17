"""
Module for connecting and handling requests to the database
"""

import time
import psycopg2
import logging

DB_NAME = "wbudowane"
DB_USER = "wbudowane"
DB_PASS = "alamakota"

class Database():
    def __init__(self):
        self.connectionCredentials = "dbname=" + DB_NAME + " user=" + DB_USER + " password=" + DB_PASS

    def createConnection():
        logging.info("Connecting to database: %s@%s", DB_USER, DB_NAME)
        try:
            self.connection = psycopg2.connect(self.connectionCredentials)
            self.cursor = self.connection.cursor()
        except:
            logging.error("Unable to connect to database")

    def closeConnection():
        logging.info("Closing database connection")
        try:
            self.cursor.close()
            self.connection.close()
        except:
            logging.error("Error while closing database connection")

    def getEmployeeIdFromTagId(tagId):
        try:
            self.cursor.execute("SELECT Employee_ID FROM Employee WHERE Tag_ID = %s ;", [tagId])
            employees = self.cursor.fetchall()
            noOfEmployees = len(employees)
            if (noOfEmployees > 1):
                logging.warn("Found multiple employees using the same card: %s", tagId)
            else if(noOfEmployees == 0):
                logging.info("No employee found with this tag: %s", tagId)
            else:
                return employees[0][0]
        except:
            logging.error("Error while fetching an employee")

    def addNewTimestampOfEmployeeId(dbConnection, employeeId):
        timestamp = psycopg2.TimestampFromTicks(int(time.time()))
        logging.info("Adding new card read to Database: employeeId: %s, timestamp: %s", employeeId, timestamp)
        try:
            self.cursor.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) VALUES (%s, %s);", (employeeId, timestamp))
            self.cursor.commit()
        except:
            logging.error("Error while adding to database")
