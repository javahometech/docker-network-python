import os
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Fetch database connection details from environment variables
        host = os.getenv('MYSQL_HOST')
        port = os.getenv('MYSQL_PORT')
        password = os.getenv('MYSQL_PASSWORD')
        database = os.getenv('MYSQL_DATABASE')
        username = os.getenv('MYSQL_USER')

        # Establish connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )

        if connection.is_connected():
            print(f"Connected to MySQL database '{database}' on host '{host}:{port}'")
            connection.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == '__main__':
    connect_to_database()
