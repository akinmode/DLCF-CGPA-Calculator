import sqlite3

class Database(object):
    def __init__(self):
        #Create connection to database for application.
        self.connection = sqlite3.connect("database\/db_mycgpa.db")
        self.pointer = self.connection.cursor()
