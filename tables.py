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
            restricted boolean NOT NULL
            FOREIGN KEY (login_id)
            REFERENCES logins (login_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE posts (
            post_id SERIAL PRIMARY KEY,
            title VARCHAR(140) NOT NULL,
            price money,
            description text,
            user_name VARCHAR(100) NOT NULL,
            user_id integer NOT NULL,
            category VARCHAR(150) NOT NULL,
            date_added timestamp NOT NULL,
            date_modified timestamp NOT NULL,
            is_live boolean NOT NULL
        )
        """,
        """
        CREATE TABLE schools (
            school_id SERIAL PRIMARY KEY,
            school_name CHAR(256) NOT NULL,
            school_address_1 VARCHAR(256) NOT NULL,
            school_address_2 VARCHAR(256) NOT NULL,
            school_state CHAR(2) NOT NULL,
        )
        """
    )
    conn = None
    try:
        # Set up credentials
        conn = psycopg2.connect(database='unified', user='unified')

        # Connect to postgres
        cur = conn.cursor()

        # Create tables
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except psycopg2.DatabaseError, error:
        print(error)
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
