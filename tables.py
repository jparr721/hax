#!/usr/bin/python3

import psycopg2
import os
import sys

def createTables():
    # Install postgres extensions if not already in there
    os.system("sudo apt-get install -y postgresql-contrib")
    os.system("sudo systemctl restart postgresql")
    commands = (
        """
        CREATE EXTENSION chkpass;
        """,
        """
        CREATE TABLE logins (
            login_id SERIAL PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            password chkpass NOT NULL
        )
        """,
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            user_name VARCHAR(100) NOT NULL,
            restricted boolean NOT NULL,
            FOREIGN KEY (user_id) REFERENCES logins (login_id) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE sample (
            post_id SERIAL PRIMARY KEY,
            title VARCHAR(140) NOT NULL,
            price money,
            description text
        )
        """,
    )
    conn = None
    try:
        # Set up credentials (change password on serverjjj)
        conn = psycopg2.connect(database='dbname', user='dbuser', host='localhost', password='dbpass')

        # Connect to postgres
        cur = conn.cursor()

        # Create tables
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
        exit()
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    euid = os.geteuid()
    if euid != 0:
        raise EnvironmentError("Please run this script as root.")
        exit()

    print("MAKE SURE YOU RUN THIS AS THE DATABASE USER")
    createTables()
