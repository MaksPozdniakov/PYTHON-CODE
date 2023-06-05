# inserting data into database:

import sqlite3

connection = sqlite3.connect(r'MyDB.db')
command = "INSERT INTO clients (ID, name, surname) VALUES (1, 'Tim', 'Jones')"
connection.execute(command)
connection.commit()  # all changes are writtten to the database
connection.close()  # always close the resource

with sqlite3.connect(r'MyDB.db') as conn:  # no need to commit, saves automatically
    command = "INSERT INTO clients (ID, name, surname) VALUES (1, 'Tim', 'Jones')"
    conn.execute(command)
