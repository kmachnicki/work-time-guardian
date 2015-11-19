#!/bin/bash

# Script to setup the database

echo "Starting postgresql service..."

sudo service postgresql start

echo "Setting up postgres database..."

echo -ne "alamakota\nalamakota" | sudo su - postgres -c 'createuser -P -e wbudowane'
sudo su - postgres -c 'createdb -e -O wbudowane wbudowane'
sudo su - postgres -c 'psql wbudowane < /home/pi/database/czaspracyBD.sql'
sudo su - postgres -c 'psql wbudowane -c "GRANT ALL ON TABLE Employee TO wbudowane;"'
sudo su - postgres -c 'psql wbudowane -c "GRANT ALL ON TABLE Passage TO wbudowane;"'
sudo su - postgres -c 'psql wbudowane -c "GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to wbudowane;"'

echo "All done"