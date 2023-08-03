import os
import mysql.connector

from flask import jsonify
from dateutil import parser

# Get the backup folder path from environment variable
sql_host = os.environ.get('SQL_HOST')
if sql_host is None or not sql_host:
    sql_host = '172.18.0.3'


# Connect to the MySQL database
def dbconnect():
    return mysql.connector.connect(
        host=sql_host,
        port=3306,
        user="root",
        password="password",
        database="fca")


def log_to_db(action, parameter, status):
    db = dbconnect()
    cursor = db.cursor()

    insert_query = "INSERT INTO log (action, parameter, status) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (action, parameter, status))
    db.commit()

    cursor.close()
    db.close()


def get(startdate, enddate):
    start_date = None
    end_date = None

    # check start date is valid
    if startdate is not None:
        start_date = parser.parse(startdate)
        startdate += " 00:00:00"

    # check end date is valid
    if enddate is not None:
        end_date = parser.parse(enddate)
        enddate += " 23:59:59"

    if start_date is not None and end_date is not None and end_date < start_date:
        raise ValueError("Start Date is < End Date")

    db = dbconnect()
    cursor = db.cursor()
    try:
        select_query = "SELECT date, action, parameter, status FROM log "

        if start_date is not None and end_date is not None:
            select_query += "WHERE date >= '" + startdate + "' AND date <= '" + enddate + "' "
        elif start_date is not None and end_date is None:
            select_query += "WHERE date >= '" + startdate + "' "
        elif start_date is None and end_date is not None:
            select_query += "WHERE date <= '" + enddate + "' "

        select_query += "ORDER BY date"
        cursor.execute(select_query)

        # Get column names, need this so we can add the keys for the JSON
        columns = [col[0] for col in cursor.description]

        # Fetch all rows from the recordset
        rows = cursor.fetchall()

        # Convert each row into a dictionary with column names as keys
        logs = []
        for row in rows:
            record = dict(zip(columns, row))
            logs.append(record)
    finally:
        cursor.close()
        db.close()

    log_to_db("GET LOGS", "", "SUCCESS")
    return jsonify(logs)


def stats():
    db = dbconnect()
    cursor = db.cursor()
    try:
        backup_count_query = "SELECT COUNT(*) FROM log WHERE action='BACKUP'"
        cursor.execute(backup_count_query)
        number_of_backups = cursor.fetchone()

        success_count_query = "SELECT COUNT(*) FROM log WHERE status='SUCCESS' AND action='BACKUP'"
        cursor.execute(success_count_query)
        number_of_successes = cursor.fetchone()

        error_count_query = "SELECT COUNT(*) FROM log WHERE status='ERROR' AND action='BACKUP'"
        cursor.execute(error_count_query)
        number_of_errors = cursor.fetchone()
    finally:
        cursor.close()
        db.close()

    log_to_db("GET STATS", "", "SUCCESS")
    return jsonify({
        "Attempted backups:": number_of_backups[0],
        "Successful backups:": number_of_successes[0],
        "Failed backups:": number_of_errors[0]
    })
dir