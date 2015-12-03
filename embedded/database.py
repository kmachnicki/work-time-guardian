"""
Module for connecting and handling requests to the database
"""

import time
import psycopg2
import logger

DB_HOST = "localhost"
DB_NAME = "wbudowane"
DB_USER = "wbudowane"
DB_PASS = "alamakota"

class Database():
    def __init__(self):
        self.connectionCredentials = "host=" + DB_HOST + " dbname=" + DB_NAME + " user=" + DB_USER + " password=" + DB_PASS

    def createConnection(self):
        logger.info("Connecting to database: " + DB_USER + "@" + DB_NAME)
        try:
            self.connection = psycopg2.connect(self.connectionCredentials)
            self.cursor = self.connection.cursor()
            #self.cursor.execute("INSERT INTO Employee(First_Name, Last_Name, Email, Password, Tag_ID) "
            #"VALUES (%s,%s,%s,%s,%s);", ["Marian", "Kowalski", "marian.kowalski@gmail.com", "test123", "3119228225113"])
        except Exception, e:
            logger.error("Unable to connect to database: " + str(e))

    def closeConnection(self):
        logger.info("Closing database connection")
        try:
            self.cursor.close()
            self.connection.close()
        except Exception, e:
            logger.error("Error while closing database connection: " + str(e))

    def getEmployeeIdFromTagId(self, tagId):
        try:
            self.cursor.execute("SELECT Employee_ID FROM Employee WHERE Tag_ID = %s ;", [tagId])
            employees = self.cursor.fetchall()
            noOfEmployees = len(employees)
            if (noOfEmployees > 1):
                logger.warn("Found multiple employees using the same card: " + tagId)
            elif(noOfEmployees == 0):
                logger.info("No employee found with this tag: " + tagId)
            else:
                return employees[0][0]
        except Exception, e:
            logger.error("Error while fetching an employee: " + str(e))

    def addNewTimestampOfEmployeeId(self, employeeId):
        timestamp = psycopg2.TimestampFromTicks(int(time.time()))
        logger.info("Adding new card read to Database: employeeId: " + str(employeeId) + ", timestamp: " + str(timestamp))
        try:
            self.cursor.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) VALUES (%s, %s);", (employeeId, timestamp))
            self.connection.commit()
        except Exception, e:
            logger.error("Error while adding to database: " + str(e))
