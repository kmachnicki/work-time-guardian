"""
Logger
"""

import logging

def setupLogger():
    logging.basicConfig(level=logging.DEBUG)

def debug(msg):
    logging.debug(msg)

def info(msg):
    logging.info(msg)

def warn(msg):
    logging.warn(msg)

def error(msg):
    logging.error(msg)
