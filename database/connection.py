import mysql.connector
from mysql.connector import errorcode
from ..config import DATABASE_CONFIG

# This code defines a function get_database_connection that establishes a connection to the MySQL database
# using the credentials and configuration settings specified in app/config.py.
# If the connection is successful, the function returns the connection object.
# If an error occurs, the function prints an error message and returns None.


def get_database_connection():
    """Get a connection to the MySQL database"""
    try:
        cnx = mysql.connector.connect(**DATABASE_CONFIG)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied for user '{}'".format(DATABASE_CONFIG['user']))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database '{}' does not exist".format(DATABASE_CONFIG['database']))
        else:
            print("Error: {}".format(err))
        return None
