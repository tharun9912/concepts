""" High level modules should not depend on low level modules for ,both should depend on abstraction """

from abc import ABC, abstractmethod

# Abstraction
class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

# Low-level module 1
class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

# Low-level module 2
class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL")

# High-level module
class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        self.database.connect()

if __name__ == "__main__":
    mysql = MySQLDatabase()
    postgres = PostgreSQLDatabase()

    app1 = Application(mysql)
    app1.start()     # Uses MySQL

    app2 = Application(postgres)
    app2.start()     # Uses PostgreSQL
