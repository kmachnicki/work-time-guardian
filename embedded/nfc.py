import MFRC522
import logger

def readNfc():
    reading = True
    while (reading):
        MIFAREReader = MFRC522.MFRC522()
        (status, tagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if (status == MIFAREReader.MI_OK):
            logger.info("Received signal")
        (status, backData) = MIFAREReader.MFRC522_Anticoll()
        if (status == MIFAREReader.MI_OK):
            readData = str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4])
            logger.info("Received Card Number: " + readData)
            reading = False
            return readData
