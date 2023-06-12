import sqlite3

# connection = sqlite3.connect(r'MyDB.db')
# command = "INSERT INTO clients (ID, name, surname) VALUES ('Tim', 'Jones', 'IT', '1999')"
# connection.execute(command)
# connection.commit()  # all changes are writtten to the database
# connection.close()  # always close the resource

# with sqlite3.connect(r'MyDB.db') as conn:  # no need to commit, saves automatically
#     command = "INSERT INTO clients (ID, name, surname) VALUES ('Tim', 'Jones', 'IT', '1999')"
#     conn.execute(command)

# L1 = [
#     ("Jessica", "Jones", "IT", 2020)
#     ("Super", "Man", "Heroes", 2018)
#     ("Wonder", "Woman", "Heroes", 2021)
# ]

# with sqlite3.connect(r'MyDB.db') as conn:
#     # "?" are placeholders for the values that ayou are going to supply in the next step
#     command = "INSERT INTO clients (ID, name, surname) VALUES ('Tim', 'Jones', 'IT', '1999')"
#     for l in L1:
#         conn.execute(command, l)


# with sqlite3.connect(r'MyDB.db') as conn:
#     # "?" are placeholders for the values that ayou are going to supply in the next step
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)  # cursor is an iterable object
#     for row in cursor:
#         print(row)

# with sqlite3.connect(r'MyDB.db') as conn:
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)
#     students = cursor.fetchall()  # returns all the rows in the table in one go
#     print(students)

# with sqlite3.connect(r'MyDB.db') as conn:
#     command = "SELECT * FROM Students WHERE Name = 'Jessica'"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)

# with sqlite3.connect(r'MyDB.db') as conn:
#     command = "SELECT Name, Surname FROM Students WHERE Year of admission = '2020'"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)

# PROJECT FROM THE BEGINNING

L1 = [
    ("Jessica", "Jones", "IT", 2020)
    ("Super", "Man", "Heroes", 2018)
    ("Wonder", "Woman", "Heroes", 2021)
]

with sqlite3.connect(r'MyDB.db') as conn:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS ('id' INTEGER, 'Name' TEXT, 'Surname' TEXT, 'Major' TEXT, 'AdmissionYear' INTEGER)")
    command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear) VALUES (?,?,?,?)"
    for l in L1:
        conn.execute(command, l)

with sqlite3.connect(r'MyDB.db') as conn:
    conn.execute(
        '''CREATE TABLE IF NOT EXISTS Students
        (id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Surname TEXT NOT NULL,
        Major TEXT, 
        AdmissionYear INTEGER)''')
    command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear) VALUES (?,?,?,?)"
    for l in L1:
        conn.execute(command, l)
