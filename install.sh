#!/bin/bash

# Script updating the system and installing all needed packages

echo "[1/9] Updating the system"
sudo apt-get update -y

echo "[2/9] Upgrading the system"
sudo apt-get upgrade -y

echo "[3/9] Installing PostgreSQL packages"
sudo apt-get install postgresql postgresql-contrib postgis gpsbabel git libsqlite3-dev libreadline-dev libpq-dev libbz2-dev zlib1g-dev libpqxx-dev libzip-dev -y

echo "[4/9] Installing Python packages"
sudo apt-get install python python-dev libjpeg-dev libfreetype6-dev python-setuptools python-pip -y

echo "[5/9] Updating Python distribution"
sudo easy_install -U distribute

echo "[6/9] Upgrading pip"
sudo pip install --upgrade pip

echo "[7/9] Installing psycopg2"
sudo pip install psycopg2

echo "[8/9] Installing RPi.GPIO"
sudo pip install RPi.GPIO

echo "[9/9] Installing SPI-Py"
sudo python ./embedded/SPI-Py/setup.py install