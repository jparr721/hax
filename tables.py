#!/usr/bin/python3

import os
import sys

# This is a ready-to-go script that will make your database tables for you on Ubuntu and Postgres
runscript = input("Have you set up your postgres roles yet?(y/n) ")
i = 0
while runscript != "y" or runscript != "n" or i < 5:
    if (i >= 5):
        print("Too many invalid attempts, exiting...")
        sys.exit()
    if (runscript == "y"):
        runScript(True)
    elif (runscript == "n"):
        runScript(False)
    print("Invalid option")
    i += 1

def initializeDatabase():
    # Install postgres extensions if not already in there
    print("\nInstalling postgresql extensions...")
    os.system("sudo apt-get install -y postgresql-contrib")

    # Enable to make sure it runs across restarts
    print("\nEnabling postgresql...")
    os.system("sudo systemctl enable postgresql")

    # Get postgres communication dependencies
    pip.main(['install', psycopg2])
    pip.main(['install', pygresql])

import psycopg2
import pygresql

def createTables():
        dbname = input("Enter database name to connect to: ")
        dbuser = input("Enter database user to connect with: ")

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
        # Set up credentials
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
def runScipt(ready):
    if (ready):
        print("MAKE SURE YOU RUN THIS AS THE DATABASE USER\n\n")
        initializeDatabase()
        createTables()
    else:
        print("Please set up the database user before running this script")
        print("=====================Instructions=========================")
        print("Follow this link and then re run this code, you must create a new role and a new database for this to work.")
        print("https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04#create-a-new-role")
        sys.exit()
