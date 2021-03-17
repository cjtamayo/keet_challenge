# Keet Health Challenge

## Coding Challenge
This is my submission for the Keet Health coding challenge. Given a user csv, the 
script creates a SQLite db and user table in that db. It then imports that CSV data.
The data is then pulled into pandas in python, where its grouped by day and a predicted
count added, then loaded back into the SQLite db.

## Running the code
Written in python3, the code can be run by calling `main.py`.

## Improved solution
Given more time and a possibly more data, some improvements may be:

* Using a Postgres DB hosted in the cloud (and imports creds as ENV VARS)
* Calculating the mean of weekends seperately from weekdays
* Place in a container, such as Docker
* If using a larger amount of data, use a tool like Spark instead of Pandas
